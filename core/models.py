from django.db                      import models
from django.contrib.gis.db          import models as gis_models
from phonenumber_field.modelfields  import PhoneNumberField

class Organization(models.Model):
    class OrganizationTypes(models.TextChoices):
        DIGITAL_INCLUSION       = 'digital_inclusion', 'Digital Inclusion'
        EDUCATION               = 'education', 'Education'
        HEALTHCARE              = 'healthcare', 'Healthcare'
        NON_PROFIT_COMMUNITY    = 'non_profit_community', 'Non-Profit / Community'
        PHILANTHROPY            = 'philanthropy', 'Philanthropy'
        PRIVATE_SECTOR          = 'private_sector', 'Private Sector'
        PUBLIC_SECTOR           = 'public_sector', 'Public Sector'
        OTHER                   = 'other', 'Other'
    name            = models.CharField(max_length=255)
    contact_name    = models.CharField(max_length=255)
    contact_email   = models.EmailField()
    contact_phone   = PhoneNumberField()
    description     = models.TextField(blank=True, null=True)
    organization_type = models.CharField(
        max_length=40,
        choices=OrganizationTypes.choices,
        default=OrganizationTypes.OTHER
    )
    url             = models.URLField(blank=True, null=True)
    slug            = models.SlugField(unique=True, blank=True, max_length=255)

    def __str__(self):
        return self.name

class Location(models.Model):
    name            = models.CharField(max_length=255)
    organization 	= models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='locations'
    )
    remote          = models.BooleanField(default=False)
    coordinates     = gis_models.PointField(blank=True, null=True, geography=True)
    street_address  = models.CharField(blank=True, max_length=255)
    suite           = models.CharField(blank=True, max_length=255)
    city            = models.CharField(blank=True, max_length=100)
    state           = models.CharField(blank=True, max_length=100)
    zip_code        = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return f"{self.organization} {self.city}"

class Program(models.Model):
    class ServiceTypes(models.TextChoices):
        DEVICE_ACQUISITION_DISTRIBUTION     = 'device_acquisition_distribution', 'Device Acquisition/Distribution'
        DIGITAL_LITERACY_SKILLS_TRAINING    = 'digital_literacy_skills_training', 'Digital Literacy/Skills Training'
        INTERNET_ACCESS_ENROLLMENT          = 'internet_access_enrollment', 'Internet Access/Enrollment Support'
        OTHER                               = 'other', 'Other'
    name            = models.CharField(max_length=255)
    description     = models.TextField(blank=True, null=True)
    organization    = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='programs'
    )
    locations = models.ManyToManyField(
        Location,
        related_name="programs",
        blank=True
    )
    service_type    = models.CharField(
        max_length=40,
        choices=ServiceTypes.choices,
        default=ServiceTypes.OTHER
    )
    url             = models.URLField(blank=True, null=True)
    slug            = models.SlugField(unique=True, blank=True, max_length=255)

    def __str__(self):
        return self.name