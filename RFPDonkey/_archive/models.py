from django.db import models
from random import randint

# Create your models here.
class system_user(models.Model):
    user_name = models.CharField(max_length=200, null=False)
    user_first_name= models.CharField(max_length=200,null=True)
    user_last_name = models.CharField(max_length=200,null=True)
    user_password = models.CharField(max_length=200, null=False)
    user_role = models.CharField(max_length=50,null=False, default = "USR")

    def __str__(self):
        return self.user_name
    

class test_class(models.Model):
    test_field = models.CharField(max_length=100,null=True)

class system_user_role(models.Model):    
    role_id = models.CharField(max_length=3,null=False, default="USR")
    role_name = models.CharField(max_length=200,null=False, default="")
    role_description = models.CharField(max_length=1000,null=True)
    def __str__(self) -> str:
        return self.role_name    

class product_type(models.Model):
    product_type_name = models.CharField(max_length=200, null = False)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.product_type_name

class product(models.Model):
    product_name  =models.CharField(max_length=200, null=False)
    product_description = models.CharField(max_length=500, null = True)
    product_type = models.ForeignKey(product_type, on_delete=models.CASCADE)
    product_active  = models.BooleanField(null=False)

    def __str__(self):
        return self.product_name
    def print_product(self):
        print(f"name:{self.product_name}\ndescription:{self.product_description}\ntype:{self.product_type}\nIsActive:{self.product_active}")
    def gen_random_items(self,how_many):
        print (f"generating: {how_many} object of type product")
        for i in range(0,how_many):
            r = randint (10,1000)
            r_name = "TEST_NAME_"+str(r)+"_"+str(i)
            r_product_description = "TEST_DESC_"+str(r)+"_"+str(i)
            r_product_type  = product_type.objects.first()
            r_product_active = True
            p = product(product_name=r_name, product_description = r_product_description, product_type=r_product_type, product_active=r_product_active)
            
            p.save()

class customer_type(models.Model):
    customer_type_name = models.CharField(max_length=200,null=False)
    customer_type_description = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_type_name
    
    

class customer(models.Model):
    customer_name = models.CharField(max_length=200,null=False)
    customer_description = models.CharField(max_length=200)
    customer_type = models.ForeignKey(customer_type, on_delete=models.CASCADE)
    customer_country = models.CharField(max_length=200, default="None")

    def __str__(self):
        return  self.customer_name

    def gen_random_items(self,how_many):
        print (f"generating: {how_many} object of type product")
        for i in range(0,how_many):
            r = randint (10,1000)
            r_name = "TEST_NAME_"+str(r)+"_"+str(i)
            r_customer_description = "TEST_DESC_"+str(r)+"_"+str(i)
            r_customer_type  = customer_type.objects.first()
            r_customer_country = "COUNTRy_"+str(r)+str(i)
            c = customer(customer_name=r_name,customer_description=r_customer_description,customer_type=r_customer_type,customer_country=r_customer_country)
            
            c.save()

    
class partner(models.Model):
    partner_name = models.CharField(max_length=200, null = False)
    partner_description = models.CharField(max_length=200)
    partner_comment = models.CharField(max_length=500)

    def __str__(self):
        return self.partner_name
    
    def gen_random_items(self,how_many):
        print (f"generating: {how_many} object of type PARTNER")
        for i in range(0,how_many):
            r = randint (10,1000)
            r_partner_name = "TEST_NAME_"+str(r)+"_"+str(i)
            r_partner_description = "TEST_DESC_"+str(r)+"_"+str(i)
            r_partner_comment = customer.objects.first()
            p = partner (partner_name=r_partner_name,partner_description=r_partner_description,partner_comment=r_partner_comment)

            p.save()



class rfp(models.Model):
    rfp_name = models.CharField(max_length=200, null=False)
    rfp_description = models.CharField(max_length=200, null=False)
    rfp_customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    rfp_winloss = models.BooleanField(default=True)
    rfp_value = models.FloatField(default=0)
    rfp_liabilities = models.CharField(max_length=300)
    rfp_comments = models.CharField(max_length=500)
    rfp_partner = models.ForeignKey(partner,on_delete=models.CASCADE)
    rfp_submitted = models.BooleanField(default=False)
    rfp_documents_folder = models.CharField(max_length=300)
    rfp_management_approved = models.BooleanField(default=True)

    def gen_random_items(self,how_many):
        print (f"generating: {how_many} object of type RFP")
        for i in range(0,how_many):
            r = randint (10,1000)
            r_name = "TEST_NAME_"+str(r)+"_"+str(i)
            r_rfp_description = "TEST_DESC_"+str(r)+"_"+str(i)
            r_rfp_customer = customer.objects.first()
            r_rfp_winloss = True
            r_rfp_value = r * 100
            r_rfp_liabilities = r
            r_rfp_comments = "COMMENT_"+str(r)+"_"+str(i)
            r_rfp_partner = partner.objects.first()
            r_rfp_submitted = True
            r_rfp_documents_folder="folder"+str(r)+"/"+str(i)+"/"
            r_rfp_management_approved = True
            r = rfp(rfp_name=r_name,
                    rfp_description = r_rfp_description,
                    rfp_customer = r_rfp_customer,
                    rfp_winloss = r_rfp_winloss,
                    rfp_value = r_rfp_value,
                    rfp_liabilities = r_rfp_liabilities,
                    rfp_comments = r_rfp_comments,
                    rfp_partner = r_rfp_partner,
                    rfp_submitted = r_rfp_submitted,
                    rfp_documents_folder = r_rfp_documents_folder,
                    rfp_management_approved = r_rfp_management_approved
                    )
            
            r.save()


    def __str__(self):
        return self.rfp_name

class questions_and_answers(models.Model):
    qa_question= models.CharField(max_length=1000,null=False)
    qa_answer = models.CharField(max_length=1000,null=False)
    qa_rfp = models.ForeignKey(rfp, on_delete=models.CASCADE)
    qa_product = models.ForeignKey(product, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return self.qa_question + "  - " + self.qa_answer

    def gen_random_items(self,how_many):
        print (f"generating: {how_many} object of type QA")
        for i in range(0,how_many):
            r = randint (10,1000)
            r_qa_question= "TEST_NAME_"+str(r)+"_"+str(i)
            r_qa_answer = "TEST_DESC_"+str(r)+"_"+str(i)
            r_qa_rfp = rfp.objects.first()
            r_qa_product = product.objects.first()
            qa = questiona_and_answers (qa_question = r_qa_question, qa_answer=r_qa_answer, qa_rfp=r_qa_rfp,qa_product=r_qa_product )
            qa.save()