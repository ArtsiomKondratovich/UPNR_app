from django.db import models

tubes = (
    ("d16", "круглая д16х2"),
    ("d12", "круглая д12х2"),
    ("14x11", "квадратная 14х11х1.5"),
)


class TubeShapes(models.Model):
    title = models.CharField(max_length=50)
    thinks = models.IntegerField()

    def __str__(self):
        return f'{self.title} x {self.thinks}'

class Machines(models.Model):
    power_of_machine = models.IntegerField()


class Inductors(models.Model):
    title = models.CharField(max_length=50)
    manufacter = models.CharField(max_length=50, blank=True)
    step = models.DecimalField(max_digits=3, decimal_places=1)
    length = models.IntegerField(default=150)
    wind_size = models.IntegerField(default=150)
    sezi_of_detail = models.CharField(max_length=50, blank=True)
    tube_shape = models.ForeignKey(TubeShapes, on_delete=models.CASCADE, blank=True)
    len_of_tube = models.IntegerField(default=150)
    notice = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'ind/{self.pk}'

class TestInductor(models.Model):
    inductor_id = models.OneToOneField(Inductors, on_delete=models.CASCADE)
    machine_id = models.OneToOneField('Machines', on_delete=models.CASCADE)
    detail = models.CharField(max_length=50)
    power = models.IntegerField()
    voltage = models.IntegerField()
    currency = models.IntegerField()
    freq = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f'{self.inductor} #{self.pk}'
