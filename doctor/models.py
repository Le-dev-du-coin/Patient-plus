from django.db import models
from django.conf import settings
#from patient.models import Patient_profile, Booking

User = settings.AUTH_USER_MODEL


# Doctor profile Start
class Doctor_profil(models.Model):
    GENDER = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),

    )
    COUNTRY = (
        ('Mali', 'Mali'),
        ('Senegal', 'Sénégal'),
        ('Côte d\'Ivoire', 'Côte D\'ivoire'),
    )
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profiDocteur", verbose_name="Photo Profil")
    gender = models.CharField(choices=GENDER, max_length=6, verbose_name="Genre")
    born_day = models.DateField(auto_now_add=False, verbose_name="Date de Naissance")
    about = models.CharField(max_length=1500, verbose_name="Qui suis-je")
    clinic_name = models.CharField(max_length=120, verbose_name="Nom de la clinique", null=True, blank=True)
    clinic_address = models.CharField(max_length=120, verbose_name="Adresse de la clinique", null=True, blank=True)
    clinic_image = models.ImageField(upload_to="image clinique")
    country = models.CharField(choices=COUNTRY, max_length=15, verbose_name="Pays", default="Mali")
    city = models.CharField(max_length=80, verbose_name="Ville")
    address = models.CharField(max_length=80, verbose_name="Quartier")
    price = models.IntegerField(default=0, verbose_name="Prix")
    services = models.ManyToManyField("Service", verbose_name="services", related_name='service')
    specialization = models.ManyToManyField("Specialization", verbose_name="Spécialisation", related_name="specialization")
    educations = models.ManyToManyField("Education", verbose_name="Educations", related_name="education")
    experiences = models.ManyToManyField("Experience", verbose_name="Expériences", related_name="experience")
    awars = models.ManyToManyField("Awars", verbose_name="Trophés", related_name="awars")
    social = models.ForeignKey("Social", on_delete= models.SET_NULL, null=True, blank=True, verbose_name="Mes réseaux", related_name="social")
    status = models.CharField(choices=STATUS, max_length=10, verbose_name="Status", default="Inactive")

    

    class Meta:
        verbose_name = ("Profil du Docteur")
        verbose_name_plural = ("Profils des Docteurs")

    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse("Doctor_profil_detail", kwargs={"pk": self.pk})



class Service(models.Model):
    doctor = models.ForeignKey(Doctor_profil, verbose_name="Docteur", on_delete=models.CASCADE, related_name="doctor_service")
    title = models.CharField(max_length=30, verbose_name="Titre")
    

    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")

    def __str__(self):
        return self.name

class Specialization(models.Model):
    doctor = models.ForeignKey(Doctor_profil, verbose_name="Docteur", on_delete=models.CASCADE,related_name="doctor_specialization")
    title = models.CharField(max_length=80, verbose_name="Titre", )
    

    class Meta:
        verbose_name = ("Spécialisation")
        verbose_name_plural = ("Spécialisations")

    def __str__(self):
        return self.name

class Education(models.Model):
    doctor = models.ForeignKey(Doctor_profil, on_delete=models.CASCADE, verbose_name="Docteur", related_name="doctor_education")
    degree = models.CharField(max_length=120, verbose_name="Diplôme")
    institute = models.CharField(max_length=150, verbose_name="Etablissement")
    year = models.DateField(auto_now_add=False, verbose_name="Année")

    class Meta:
        verbose_name = ("Education")
        verbose_name_plural = ("Educations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Education_detail", kwargs={"pk": self.pk})


class Experience(models.Model):
    doctor = models.ForeignKey(Doctor_profil, on_delete=models.CASCADE, verbose_name="Docteur", related_name="doctor_experience")
    jobTitle = models.CharField(max_length=60, verbose_name="Poste occupé")
    startYear = models.DateField(auto_now_add=False)
    endYear = models.DateField(auto_now_add=False)
    

    class Meta:
        verbose_name = ("Experience")
        verbose_name_plural = ("Experiences")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Experience_detail", kwargs={"pk": self.pk})

class Awars(models.Model):
    doctor = models.ForeignKey(Doctor_profil, verbose_name="Docteur", on_delete=models.CASCADE, related_name="doctor_awars")
    title = models.CharField(max_length=120, verbose_name="Titre")
    description = models.CharField(max_length=1500, verbose_name="Description")
    

    class Meta:
        verbose_name = ("Trophé")
        verbose_name_plural = ("Trophés")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Awars_detail", kwargs={"pk": self.pk})

class Social(models.Model):
    doctor = models.ForeignKey(Doctor_profil, on_delete=models.CASCADE, verbose_name="Docteur", related_name="doctor_social")
    facebook_link = models.URLField( max_length=250, null=True, blank=True, verbose_name="Facebook")
    twitter_link = models.URLField(max_length=250, null=True, blank=True, verbose_name="X")
    instagram_link = models.URLField(max_length=250, null=True, blank=True, verbose_name="Instagram")
    linkedin_link = models.URLField(max_length=250, null=True, blank=True, verbose_name="Linkedin")


    class Meta:
        verbose_name = ("Reseau Social")
        verbose_name_plural = ("Reseaux Sociaux")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Social_detail", kwargs={"pk": self.pk})

# Doctor profile End


# Appointment
class Appointment(models.Model):
    STATUS = (
        ('Complète', 'Complète'),
        ('Annuler', 'Annuler')
    )

    doctor = models.ForeignKey(Doctor_profil, on_delete=models.CASCADE, verbose_name="Docteur")
    id_appointment = models.CharField(max_length=50, verbose_name="ID Rendez-vous")
    appointment_date = models.DateField(auto_now_add=False, verbose_name="Date du Rendez-vous")
    appointment_time = models.TimeField(auto_now_add=False, verbose_name="Heure du Rendez-vous")
    booking_date = models.ForeignKey("Booking", on_delete=models.SET_NULL, null=True, verbose_name="Date de réservation")
    status = models.CharField(choices=STATUS, max_length=20, verbose_name="Status")
    paid_amount = models.ForeignKey("Invoice", on_delete=models.SET_NULL, null=True, verbose_name="Montant payé", related_name="payement")
    is_confirm = models.BooleanField(default=False, verbose_name="Confirmer")
    is_cancel = models.BooleanField(default=False, verbose_name="Annuler")
    patient = models.ForeignKey("Patient_profile", on_delete=models.SET_NULL, null=True, verbose_name="Patient")

    

    class Meta:
        verbose_name = ("Rendez-vous")
        verbose_name_plural = ("Rendez-vous")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Appointment_detail", kwargs={"pk": self.pk})




class My_patient(models.Model):
    patient = models.ForeignKey(Appointment, verbose_name=("Patient"), on_delete=models.SET_NULL, null=True)
    id_patient = models.CharField(max_length=80, verbose_name="ID patient")
    

    class Meta:
        verbose_name = ("Mon Patient")
        verbose_name_plural = ("Mes Patients")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("MyPatient_detail", kwargs={"pk": self.pk})



class Schedule_timimg(models.Model):
    TIME_SLOT_DURATION = (
        (15, "15 mins"),
        (30, "30 mins"),
        (45, "45 mins"),
        (60, "1 heures")
    )

    SCHEDULE_DAYS = (
        ('Lundi', "Lundi"),
        ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'),
        ('Vendredi', 'Vendredi'),
        ('Samedi', 'Samedi'),
        ('Dimanche', 'Dimanche')
    )
    doctor = models.ForeignKey(Doctor_profil, on_delete=models.CASCADE, verbose_name="Docteur") 
    time_slot_duration = models.IntegerField(choices=TIME_SLOT_DURATION)
    schedule_days = models.CharField(max_length=50, choices=SCHEDULE_DAYS, verbose_name="Date")
    time_slot = models.ManyToManyField("Time_slot", blank=True, verbose_name="Heure")

    class Meta:
        verbose_name = ("Schedule_timimg")
        verbose_name_plural = ("Schedule_timimg")



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Schedule_timimg_detail", kwargs={"pk": self.pk})


class Time_slot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.ForeignKey(Schedule_timimg, on_delete=models.SET_NULL, null=True, blank=True, related_name="day")
    

    class Meta:
        verbose_name = ("Time_slot")
        verbose_name_plural = ("Time_slots")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Time_slot_detail", kwargs={"pk": self.pk})


class Invoice(models.Model):
    invoice_id = models.CharField(max_length=50, null=True, blank=True, verbose_name="Id Facture")
    description = models.CharField(max_length=120, verbose_name="Description")
    date_invoice = models.DateTimeField(auto_now_add=True, verbose_name='date de facturation')
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    doctor = models.ForeignKey(Doctor_profil, on_delete=models.CASCADE, verbose_name="Docteur")
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, verbose_name="Rendez-vous")
    patient = models.ForeignKey("Patient_profile", on_delete=models.SET_NULL, null=True, verbose_name="invoice_patient")
    

    class Meta:
        verbose_name = ("Facture")
        verbose_name_plural = ("Factures")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Invoice_detail", kwargs={"pk": self.pk})


class Medical_record(models.Model):
    id_record = models.CharField(max_length=120, verbose_name="ID Ordonnance")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date")
    description = models.CharField(max_length=1500, verbose_name="Description")
    attachement = models.FileField(upload_to="attachement", verbose_name="Documents Médical")
    create_by = models.ForeignKey(Doctor_profil, on_delete=models.CASCADE, verbose_name="Créer par")
    patient = models.ForeignKey("Patient_profile", on_delete=models.CASCADE, verbose_name="Patient")
    

    class Meta:
        verbose_name = ("Document Médical")
        verbose_name_plural = ("Documents Médicaux")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Medical_record_detail", kwargs={"pk": self.pk})

########### Patient Models ###############

class Patient_profile(models.Model):
    COUNTRY = (
        ('Mali', 'Mali'),
        ('Burkina', 'Burkina')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Patient")
    born_day = models.DateField(auto_now_add=False, verbose_name="Date de naissance")
    blood_group = models.CharField(max_length=3, verbose_name="Groupe Sanguin")
    address = models.CharField(max_length=120, verbose_name="Adresse")
    city = models.CharField(max_length=80, verbose_name="Ville")
    country = models.CharField(choices=COUNTRY, max_length=15, verbose_name="Pays")
    image = models.ImageField(upload_to="patient_profile", verbose_name="Image patient")


    class Meta:
        verbose_name = ("Profil du Patient")
        verbose_name_plural = ("Profil des Patients")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Patient_profile_detail", kwargs={"pk": self.pk})


class Booking(models.Model):
    VIDEO_CALL = (
        ('Oui','Oui'),
        ('Non', 'Non')
    )

    doctor = models.ForeignKey(Doctor_profil, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Docteur")
    date = models.DateField(auto_now_add=False, verbose_name="Date")
    start_time = models.TimeField(auto_now_add=False, verbose_name="Heure")
    booking_fee = models.IntegerField(verbose_name="Frais de reservation")
    consulting_fee = models.IntegerField(verbose_name="Frais consultation")
    video_call = models.CharField(choices=VIDEO_CALL, max_length=5, default='Oui', verbose_name="Appel Vidéo")
    booking_date = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient_profile, on_delete=models.CASCADE, verbose_name="Reservation Patient")
    

    class Meta:
        verbose_name = ("Reservation")
        verbose_name_plural = ("Reservations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Booking_detail", kwargs={"pk": self.pk})



class Billing(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, verbose_name='Facture')
    doctor = models.ForeignKey(Doctor_profil, on_delete=models.CASCADE, verbose_name='Docteur')
    patient = models.ForeignKey(Patient_profile, on_delete=models.CASCADE, verbose_name='Patient')
    

    class Meta:
        verbose_name = ("Payement")
        verbose_name_plural = ("Payements")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Billing_detail", kwargs={"pk": self.pk})


class Favorite(models.Model):
    doctor = models.ForeignKey(Doctor_profil, on_delete=models.CASCADE, verbose_name='Docteur')
    patient = models.ForeignKey(Patient_profile, on_delete=models.CASCADE, verbose_name='Patient')
    

    class Meta:
        verbose_name = ("Favorie")
        verbose_name_plural = ("Favories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Favorite_detail", kwargs={"pk": self.pk})
