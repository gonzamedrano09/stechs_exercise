from django.db import models


class DocsisUpdate(models.Model):
    modem_macaddr = models.CharField(primary_key=True, max_length=15)
    ipaddr = models.CharField(unique=True, max_length=16)
    cmts_ip = models.CharField(max_length=16)
    agentid = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    mce_concat = models.CharField(max_length=3, blank=True, null=True)
    mce_ver = models.CharField(max_length=4, blank=True, null=True)
    mce_frag = models.CharField(max_length=3, blank=True, null=True)
    mce_phs = models.CharField(max_length=3, blank=True, null=True)
    mce_igmp = models.CharField(max_length=3, blank=True, null=True)
    mce_bpi = models.CharField(max_length=4, blank=True, null=True)
    mce_ds_said = models.PositiveIntegerField(blank=True, null=True)
    mce_us_sid = models.PositiveIntegerField(blank=True, null=True)
    mce_filt_dot1p = models.CharField(max_length=3, blank=True, null=True)
    mce_filt_dot1q = models.CharField(max_length=3, blank=True, null=True)
    mce_tetps = models.PositiveIntegerField(blank=True, null=True)
    mce_ntet = models.PositiveIntegerField(blank=True, null=True)
    mce_dcc = models.CharField(max_length=3, blank=True, null=True)
    thetime = models.DateTimeField()
    offer_time = models.DateTimeField(blank=True, null=True)
    ack_time = models.DateTimeField(blank=True, null=True)
    net_id = models.PositiveSmallIntegerField()
    cluster_id = models.PositiveSmallIntegerField()
    ra_id = models.PositiveSmallIntegerField()
    vsi_devtype = models.CharField(max_length=255)
    vsi_esafetypes = models.CharField(max_length=255)
    vsi_serialno = models.CharField(max_length=255)
    vsi_hwver = models.CharField(max_length=255)
    vsi_swver = models.CharField(max_length=255)
    vsi_bootrom = models.CharField(max_length=255)
    vsi_oui = models.CharField(max_length=255)
    vsi_model = models.CharField(max_length=255)
    vsi_vendor = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "docsis_update"
