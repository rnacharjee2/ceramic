from django.db import models

# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Shape(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Code(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class ItemName(models.Model):
    name = models.CharField(max_length=100)
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE)
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    shapeCode = models.CharField(max_length=100)
    description = models.TextField()
    weight = models.FloatField()
    diameter = models.FloatField()
    height = models.FloatField()
    photo = models.ImageField(upload_to='images/', blank=True)

    def save(self, *args, **kwargs):
        self.shapeCode = self.shape.name + self.code.name
        super(ItemName, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RawMaterialIncoming(models.Model):
    name = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return self.name


class RawMaterialOutgoing(models.Model):
    name = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return self.name
