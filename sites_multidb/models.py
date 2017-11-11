from django.db import models


class DBConfig(models.Model):
    """
    Stores configuration information for an external database.
    """
    # Flag for router
    SITES_MULTIDB_USE_DEFAULT_DB = True

    DB_ENGINE_CHOICES = (
        ('django.db.backends.postgresql', 'PostgreSQL'),
        ('django.db.backends.mysql', 'MySQL'),
        ('django.db.backends.sqlite3', 'SQLite'),
        ('django.db.backends.oracle', 'Oracle')
    )

    name = models.CharField(unique=True, max_length=50)
    engine = models.CharField(max_length=100, choices=DB_ENGINE_CHOICES)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    host = models.CharField(max_length=100, null=True, blank=True)
    port = models.PositiveIntegerField(null=True, blank=True)

    def as_config_dict(self):
        """
        :return: Dictionary in Django database config format
        """
        d = {
            'NAME': self.name,
            'ENGINE': self.engine,
            'USER': self.user,
            'PASSWORD': self.password
        }
        if self.host:
            d['HOST'] = self.host
        if self.port:
            d['PORT'] = self.port
        return d

    def __str__(self):
        return self.name + '/' + self.user

    class Meta:
        verbose_name = "Database configuration"
        verbose_name_plural = "Database configurations"
