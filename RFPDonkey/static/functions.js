function Test()
{
 
  f = document.forms.frm;
  f.action = "/test/1/2/";
  f.method = "POST";
  f.submit();
}

function ProductTypeLookUp()
{
  f=document.forms.frm;
  p_type = f.product_type.value;
  if (p_type=="")
  {
    p_type="none"
  }
  let url = "/product_type_lookup/"+p_type+"/"
  window.open(url, '_blank', 'location=yes,height=570,width=520,scrollbars=yes,status=yes');
}


function ProductTypeAdd()
{
  
  f = document.forms.frm;
  f.action="/product_type_add/";
  f.method="POST";
  f.submit();
}

function ProdductTypeDelete()
{
  f = document.forms.frm;
  f.action="/product_type_del/";
  f.method="POST";
  f.submit();
}

function ProductTypeUpdate()
{
  f = document.forms.frm;
  f.action="/product_type_update/";
  f.method="POST";
  f.submit();
}

function ProductTypeClose()
{
  window.close();
}


function CustomerTypeLookUp()
{
  
  f=document.forms.frm;
  c_type = f.customer_type.value;
  if (c_type=="")
  {
    c_type="none"
  }
  let url = "/customer_type_lookup/"+c_type+"/"
  window.open(url, '_blank', 'location=yes,height=570,width=520,scrollbars=yes,status=yes');

}

function CustomerTypeAdd()
{
  f = document.forms.frm;
  f.action="/customer_type_add/";
  f.method="POST";
  f.submit();
}

function CustomerTypeDelete()
{
  f = document.forms.frm;
  f.action = "/customer_type_del/";
  f.method = "POST";
  f.submit();
}

function CustomerTypeClose()
{
  window.close();
}

function CustomerTypeUpdate()
{
  f = document.forms.frm;
  f.action = "/customer_type_update/";
  f.method = "POST";
  f.submit();
}

function PartnerLookUp()
{
  f=document.forms.frm;
  p_type = f.rfp_partner.value;
  if (p_type=="")
  {
    p_type="none"
  }
  let url = "/partner_lookup/"+p_type+"/"
  window.open(url, '_blank', 'location=yes,height=570,width=520,scrollbars=yes,status=yes');
}

function PartnerLUAdd()
{
  f = document.forms.frm;
  f.action="/partner_lu_add/";
  f.method="POST";
  f.submit();
}

function PartnerLUClose()
{
  window.close()
}

function PartnerLUDelete()
{
  f = document.forms.frm;
  f.action="/partner_lu_del/";
  f.method="POST";
  f.submit();
}

function PartnerLUUpdate()
{
  f = document.forms.frm;
  f.action="/partner_lu_update/";
  f.method="POST";
  f.submit();
}

function TenderLookUp()
{
  f=document.forms.frm;
  t = f.qa_tender.value;
  if (t=="")
  {
    t="none"
  }
  let url = "/tender_lookup/"+t+"/"
  window.open(url, '_blank', 'location=yes,height=570,width=520,scrollbars=yes,status=yes');
}

function TenderLUClose()
{
  window.close();
}

function ProductLookUp()
{
  
  f=document.forms.frm;
  p = f.qa_product.value;
  if (p=="")
  {
    p="none"
  }
  let url = "/product_lookup/"+p+"/"
  window.open(url, '_blank', 'location=yes,height=570,width=520,scrollbars=yes,status=yes');
}

function ProductLUClose()
{
  window.close()
}

function Login()
{
  f = document.forms.frm;
  f.action="/authenticate/";
  f.method="POST";
  f.submit();
}

function ProdNew()
{
  f=document.forms.frm;
  f.product_id.value="";
  f.product_name.value="";
  f.product_description.value="";
  f.product_type.options[0].selected = true;
  f.product_active.checked = false
}

function ProdDelete(c_page,t_page,direction)
{
  c_page = c_page + direction;
  f = document.forms.frm;
  f.action = "/product_delete/"+c_page+"/"+t_page+"/";
  f.method = "POST";
  f.submit();
}

function ProdSearch(c_page,t_page,direction)
{
  c_page = c_page + direction;
  f = document.forms.frm;
  f.action = "/prod_search/"+c_page+"/"+t_page+"/";
  f.method = "POST";
  f.submit();
}

function ProdSelection(id,name,description,type,status)
{
  
  
  f=document.forms.frm;
  f.product_id.value=id;
  f.product_name.value=name;
  f.product_description.value=description;
  f.product_type.value=type;
  if ( status=='True')
    f.product_active.checked = true
  else
  f.product_active.checked = false
}

function ProdAdd(c_page,t_page,direction)
{
  c_page = c_page + direction;
  f = document.forms.frm;
  f.action = "/product_add/"+c_page+"/"+t_page+"/";
  f.method = "POST";
  f.submit();
}

function ProdUpdate(c_page,t_page,direction)
{
  c_page = c_page + direction;
  f = document.forms.frm;
  f.action = "/product_update/"+c_page+"/"+t_page+"/";
  f.method = "POST";
  f.submit();
}

function CustAdd(c_page,t_page,direction)
{
  c_page = c_page + direction;
  f = document.forms.frm;
  f.action = "/customer_add/"+c_page+"/"+t_page+"/";
  f.method = "POST";
  f.submit();
}


function CustUpdate(c_page,t_page,direction)
{
  c_page = c_page + direction;
  f = document.forms.frm;
  f.action = "/customer_update/"+c_page+"/"+t_page+"/";;
  f.method = "POST";
  f.submit();
}

function CustDelete(c_page,t_page,direction)
{
  c_page = c_page + direction;
  f = document.forms.frm;
  f.action = "/customer_delete/"+c_page+"/"+t_page+"/";
  f.method = "POST";
  f.submit();
}

function CustSearch(c_page,t_page,direction)
{
  c_page = c_page + direction;
  f = document.forms.frm;
  f.action = "/customer_search/"+c_page+"/"+t_page+"/";
  f.method = "POST";
  f.submit();
}

function CustSelection(id,name,description,c_type,country)
{
  
  f = document.forms.frm;
  f.customer_id.value = id;
  f.customer_name.value = name;
  f.customer_description.value = description;
  f.customer_type.value = c_type;
  f.customer_country.value = country;

}

function CustNew()
{
  f = document.forms.frm;
  f.customer_id.value = '';
  f.customer_name.value = '';
  f.customer_description.value = '';
  f.customer_type.options[0].selected=true;
  f.customer_country.value = '';
}

function PartSelection(id,name,description, comment)
{
  f = document.forms.frm;
  f.partner_id .value= id;
  f.partner_name.value = name;
  f.partner_description.value = description;
  f.partner_comment.value = comment;
}

function PartAdd(c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.action = "/partner_add/"+c_page+"/"+t_page+"/";
  f.method = "POST";
  f.submit();
}

function PartNew()
{
  f = document.forms.frm;
  f.partner_id.value = '';
  f.partner_name.value ='';
  f.partner_description.value = '';
  f.partner_comment.value = '';

}

function PartDelete(c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.action = "/partner_delete/"+c_page+"/"+t_page+"/";
  f.method = "POST";
  f.submit();
}

function PartUpdate(c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.action = "/partner_update/"+c_page+"/"+t_page+"/";
  f.method = "POST";
  f.submit();
}

function PartSearch(c_page,t_page,direction)
{

  c_page = c_page+direction;
  f = document.forms.frm;
  f.action = "/partner_search/"+c_page+"/"+t_page+"/";
  f.method = "POST";
  f.submit();
}

function MainSearch() 
{
  f = document.forms.frm;
  question = f.elements.txtQuestion.value;
  f.action = "/rfp_qa_list/";
  f.method = "POST";
  f.submit();
}

function Tender(c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.method ="POST";
  f.action="/rfp_new/"+c_page+"/"+t_page+"/";
  f.submit();
}

function QAAdd(c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.method ="POST";
  f.action="/qa_add/"+c_page+"/"+t_page+"/";
  f.submit();
}

function QAUpdate(c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.method ="POST";
  f.action="/qa_update/"+c_page+"/"+t_page+"/";
  f.submit();
}

function QANew()
{
  f = document.forms.frm;
  f.qa_id.value = "";
  f.qa_question.value="";
  f.qa_answer.value = "";
  f.qa_tender.value = "";
  f.qa_product.value = "";
}

function QASearch(c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.method = "POST";
  f.action = "/qa_search/"+c_page+"/"+t_page+"/";
  f.submit();
}

function QASelection(id,question,answer,tender,product)
{
  f = document.forms.frm;
  f.qa_id.value = id;
  f.qa_question.value=question;
  f.qa_answer.value = answer;
  f.qa_tender.value = tender;
  f.qa_product.value = product;

}

function QADelete(c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.method = "POST";
  f.action = "/qa_delete/"+c_page+"/"+t_page+"/";
  f.submit();
}

function RfpAdd(c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.method ="POST";
  f.action="/rfp_add/"+c_page+"/"+t_page+"/";
  f.submit();
}

function RfpSelection(id,name,description,customer,winloss,value,liabilitie,comments,partner,submitted,folder,approved)
{

  f = document.forms.frm;
  f.rfp_id.value = id;
  f.rfp_name.value=name;
  f.rfp_description.value = description;
  f.rfp_customer_name.value = customer;
  if (winloss=='True')
    f.rfp_winloss.checked=true;
  f.rfp_value.value= value;
  f.rfp_liabilities.value= liabilitie;
  f.rfp_comments.value = comments;
  f.rfp_partner.value = partner;
  if (submitted=='True')
    f.rfp_submitted.checked = true;
  f.rfp_documents_folder.value = folder;
  if (approved=='True')
    f.rfp_management_approved.checked=true
}

function RfpDelete(c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.method ="POST";
  f.action="/rfp_delete/"+c_page+"/"+t_page+"/";
  f.submit();
}


function RfpUpdate(c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.method ="POST";
  f.action="/rfp_update/"+c_page+"/"+t_page+"/";
  f.submit();
}

function RfpNew()
{
  f = document.forms.frm;
  f.rfp_id.value = '';
  f.rfp_name.value='';
  f.rfp_description.value = '';
  f.rfp_customer_name.value = '';
  f.rfp_winloss.checked=false;
  f.rfp_value.value= '';
  f.rfp_liabilities.value= '';
  f.rfp_comments.value = '';
  f.rfp_partner.value = '';
  f.rfp_submitted.checked = false;
  f.rfp_documents_folder.value = '';
  f.rfp_management_approved.checked=false;
}

function RfpSearch(c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.method ="POST";
  f.action="/rfp_search/"+c_page+"/"+t_page+"/";
  f.submit();
}

function QA(c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.method ="POST";
  f.action="/qa_new/"+c_page+"/"+t_page+"/";
  f.submit();
}

function Product (c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.method ="POST";
  f.action="/product_new/"+c_page+"/"+t_page+"/";
  f.submit();
}


function Customer(c_page,t_page,direction)
{
  c_page = c_page + direction;
  f = document.forms.frm;
  f.method ="POST";
  f.action="/customer_new/"+c_page+"/"+t_page+"/";
  f.submit();
}

function Partner(c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.method ="POST";
  f.action="/partner_new/"+c_page+"/"+t_page+"/";
  f.submit();
}

function MainAdd()
{
  f = document.forms.frm;
  // question = f.elements.txtQuestion.value;
  f.txtProduct_value.value = f.txtProduct.value;
  f.txtRfp_value.value=f.txtRfp.value;
  f.action = "/rfp_addrecord/";
  f.method="POST";
  f.submit();
  
}

function MainUpdate(id)
{

  f = document.forms.frm;
  f.txtProduct_value.value = f.txtProduct.value;
  f.txtRfp_value.value=f.txtRfp.value;
  f.method = "POST";
  f.action = "/rfp_updaterecord/";
  f.submit();
}

function MainDelete()
{
  f = document.forms.frm;
  f.method ="POST";
  f.action="/rfp_deleterecord/";
  f.submit();
  
}

function MainReset()
{
 
  f = document.forms.frm;
  f.method ="POST";
  f.action="/rfp_kb/0";
  f.submit();
  
}

function MainNew()
{
  f = document.forms.frm;
  f.action = "/rfp_kb/0";
  f.method="POST";
  f.submit();
}

function RoleLookUp()
{
  alert ("Function not implemented yet !")
}

function User(c_page,t_page,direction)
{
  c_page = c_page+direction;
  f = document.forms.frm;
  f.method ="POST";
  f.action="/user_new/"+c_page+"/"+t_page+"/";
  f.submit();
}

function UserSearch()
{
  f = document.forms.frm;
  f.method ="POST";
  f.action="/user_search/";
  f.submit(); 
}

function UserSelection(id,user_name,user_first_name,user_last_name,user_password,user_role)
{
  f  = document.forms.frm;
  f.user_id.value = id;
  f.user_name.value =user_name;
  f.user_password.value=user_password;
  f.user_first_name.value = user_first_name;
  f.user_last_name.value=user_last_name;
  f.user_role.value = user_role;
}

function UserNew()
{
  f  = document.forms.frm;
  f.user_id.value = "";
  f.user_name.value ="";
  f.user_password.value="";
  f.user_first_name.value = "";
  f.user_last_name.value="";
  f.user_role.value = "";
}

function UserDelete()
{
  f = document.forms.frm;
  f.method ="POST";
  f.action="/user_delete/";
  f.submit(); 
}

function  UserAdd()
{
  f = document.forms.frm;
  f.method="POST";
  f.action="/user_add/";
  f.submit();
}

function UserUpdate()
{
  f = document.forms.frm;
  f.method="POST";
  f.action="/user_update/";
  f.submit();
}