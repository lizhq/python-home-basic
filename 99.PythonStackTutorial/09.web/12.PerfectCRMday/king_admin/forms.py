#__author:  Administrator
#date:  2017/1/10

from django.utils.translation import ugettext as _
from django.forms import forms,ModelForm
from django.forms import ValidationError
from crm import models

class CustomerModelForm(ModelForm):
    class Meta:
        model =  models.Customer
        fields = "__all__"







def create_model_form(request,admin_class):
    '''动态生成MODEL FORM'''
    def __new__(cls, *args, **kwargs):

        # super(CustomerForm, self).__new__(*args, **kwargs)
        #print("base fields",cls.base_fields)
        for field_name,field_obj in cls.base_fields.items():
            #print(field_name,dir(field_obj))
            field_obj.widget.attrs['class'] = 'form-control'
            # field_obj.widget.attrs['maxlength'] = getattr(field_obj,'max_length' ) if hasattr(field_obj,'max_length') \
            #     else ""
            if not hasattr(admin_class,"is_add_form"): #代表这是添加form,不需要disabled
                if field_name in admin_class.readonly_fields:
                    field_obj.widget.attrs['disabled'] = 'disabled'

            if hasattr(admin_class,"clean_%s" % field_name):
                field_clean_func = getattr(admin_class,"clean_%s" %field_name)
                setattr(cls,"clean_%s"%field_name, field_clean_func)


        return ModelForm.__new__(cls)

    def default_clean(self):
        '''给所有的form默认加一个clean验证'''
        print("---running default clean",admin_class)
        print("---running default clean",admin_class.readonly_fields)
        print("---obj instance",self.instance.id)

        error_list = []
        if self.instance.id: # 这是个修改的表单
            for field in admin_class.readonly_fields:
                field_val = getattr(self.instance,field) #val in db
                if hasattr(field_val,"select_related"): #m2m
                    m2m_objs = getattr(field_val,"select_related")().select_related()
                    m2m_vals = [i[0] for i in m2m_objs.values_list('id')]
                    set_m2m_vals = set(m2m_vals)
                    set_m2m_vals_from_frontend = set([i.id for i in self.cleaned_data.get(field)])
                    print("m2m",m2m_vals,set_m2m_vals_from_frontend)
                    if set_m2m_vals != set_m2m_vals_from_frontend:
                        # error_list.append(ValidationError(
                        #     _('Field %(field)s is readonly'),
                        #     code='invalid',
                        #     params={'field': field},
                        # ))
                        self.add_error(field,"readonly field")
                    continue

                field_val_from_frontend =  self.cleaned_data.get(field)
                #print("cleaned data:",self.cleaned_data)
                print("--field compare:",field, field_val,field_val_from_frontend)
                if field_val != field_val_from_frontend:
                    error_list.append( ValidationError(
                                _('Field %(field)s is readonly,data should be %(val)s'),
                                code='invalid',
                                params={'field': field,'val':field_val},
                           ))


        #readonly_table check
        if admin_class.readonly_table:
            raise ValidationError(
                                _('Table is  readonly,cannot be modified or added'),
                                code='invalid'
                           )

        #invoke user's cutomized form validation
        self.ValidationError = ValidationError
        response = admin_class.default_form_validation(self)
        if response:
            error_list.append(response)

        if error_list:
            raise ValidationError(error_list)

    class Meta:
        model = admin_class.model
        fields = "__all__"
        exclude = admin_class.modelform_exclude_fields
    attrs = {'Meta':Meta}
    _model_form_class =  type("DynamicModelForm",(ModelForm,),attrs)
    setattr(_model_form_class,'__new__',__new__)
    setattr(_model_form_class,'clean',default_clean)

    print("model form",_model_form_class.Meta.model )
    return _model_form_class