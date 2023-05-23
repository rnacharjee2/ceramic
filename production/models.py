from django.db import models

# Create your models here.
SHIFT_CHOICES = [
    (1, 'A Shift'),
    (2, 'B Shift'),
    (3, 'C Shift'),
]


class MeasurementUnit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Shape(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Code(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ItemName(models.Model):
    name = models.CharField(max_length=100)
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE)
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    shapeCode = models.CharField(max_length=10, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    weight = models.FloatField()
    diameter = models.FloatField()
    height = models.FloatField()
    photo = models.ImageField(upload_to='images/items/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.shapeCode = self.code.name + self.shape.name
        super(ItemName, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RawMaterialIncoming(models.Model):
    name = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)
    challanNo = models.CharField(max_length=100)
    challanDate = models.DateField()

    def __str__(self):
        return self.name


class RawMaterialOutgoing(models.Model):
    name = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Machine(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class MachineCapacity(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemName, on_delete=models.CASCADE)
    capacity = models.FloatField()
    unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)

    def __str__(self):
        return self.machine.name + self.item.name


class JiggerProduction(models.Model):
    item = models.ForeignKey(ItemName, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    shift = models.PositiveIntegerField(choices=SHIFT_CHOICES)
    quantity = models.PositiveIntegerField()
    forming_loss = models.PositiveIntegerField()
    production_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item.name
