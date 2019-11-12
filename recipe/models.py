from django.db import models

class Menu(models.Model):
    item_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.item_name


class Person(models.Model):
    person_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.person_name


class Kharabath(models.Model): 
    assigned= models.ForeignKey( Person, on_delete=models.CASCADE,)
    process_step = models.CharField(max_length=500)
    schedule = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.process_step)


class Kesaribath(models.Model): 
    assigned= models.ForeignKey( Person, on_delete=models.CASCADE,)
    process_step = models.CharField(max_length=500)
    schedule = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.process_step)


class RoundIdli(models.Model): 
    assigned= models.ForeignKey( Person, on_delete=models.CASCADE,)
    process_step = models.CharField(max_length=500)
    schedule = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.process_step)


class TatteIdli(models.Model): 
    assigned= models.ForeignKey( Person, on_delete=models.CASCADE,)
    process_step = models.CharField(max_length=500)
    schedule = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.process_step)



class RiceBath(models.Model): 
    assigned= models.ForeignKey( Person, on_delete=models.CASCADE,)
    process_step = models.CharField(max_length=500)
    schedule = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.process_step)



class Bisibelebath(models.Model): 
    assigned= models.ForeignKey( Person, on_delete=models.CASCADE,)
    process_step = models.CharField(max_length=500)
    schedule = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.process_step)



class Puliyogare(models.Model): 
    assigned= models.ForeignKey( Person, on_delete=models.CASCADE,)
    process_step = models.CharField(max_length=500)
    schedule = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.process_step)



class Avalakki(models.Model): 
    assigned= models.ForeignKey( Person, on_delete=models.CASCADE,)
    process_step = models.CharField(max_length=500)
    schedule = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.process_step)



class Mandakki(models.Model): 
    assigned= models.ForeignKey( Person, on_delete=models.CASCADE,)
    process_step = models.CharField(max_length=500)
    schedule = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.process_step)



class UddinaVada(models.Model): 
    assigned= models.ForeignKey( Person, on_delete=models.CASCADE,)
    process_step = models.CharField(max_length=500)
    schedule = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.process_step)


class MasalaVada(models.Model): 
    assigned= models.ForeignKey( Person, on_delete=models.CASCADE,)
    process_step = models.CharField(max_length=500)
    schedule = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.process_step)


class DosaD(models.Model): 
    assigned= models.ForeignKey( Person, on_delete=models.CASCADE,)
    process_step = models.CharField(max_length=500)
    schedule = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.process_step)


class Paddu(models.Model): 
    assigned= models.ForeignKey( Person, on_delete=models.CASCADE,)
    process_step = models.CharField(max_length=500)
    schedule = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.process_step)


class Generic(models.Model): 
    assigned= models.ForeignKey( Person, on_delete=models.CASCADE,)
    process_step = models.CharField(max_length=500)
    schedule = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.process_step)

