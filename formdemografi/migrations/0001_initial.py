# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 07:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(blank=True, choices=[('POSTAL', 'Postal'), ('PHYSICAL', 'Fisik'), ('BOTH', 'Postal dan Fisik')], help_text='Tipe alamat', max_length=10)),
                ('text', models.CharField(blank=True, help_text='Alamat Lengkap', max_length=200)),
                ('line', models.CharField(blank=True, help_text='Nama jalan, nomor, P.O. Box, dan lainnya', max_length=200)),
                ('city', models.CharField(blank=True, help_text='Nama kota', max_length=100)),
                ('district', models.CharField(blank=True, help_text='District name (aka county)', max_length=100)),
                ('state', models.CharField(blank=True, help_text='Sub-unit of country (abbreviations ok)', max_length=100)),
                ('postalCode', models.CharField(blank=True, help_text='Kode Pos', max_length=20)),
                ('country', models.CharField(blank=True, help_text='Negara', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='antrian',
            fields=[
                ('no_antrian', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentType', models.CharField(blank=True, max_length=200)),
                ('url', models.CharField(blank=True, max_length=200)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('creation', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CodeableConcept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=245)),
            ],
        ),
        migrations.CreateModel(
            name='Coding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(blank=True, max_length=200)),
                ('version', models.CharField(blank=True, max_length=200)),
                ('code', models.CharField(blank=True, max_length=200)),
                ('display', models.CharField(blank=True, max_length=245)),
                ('userSelected', models.BooleanField()),
                ('codeableconcept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.CodeableConcept')),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_edit', models.BooleanField(default=False)),
                ('status_sinkronisasi', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(blank=True, null=True)),
                ('dateRecorded', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(help_text='kode', max_length=20)),
                ('category', models.CharField(blank=True, choices=[('complaint', 'Keluhan'), ('symptom', 'Gejala'), ('finding', 'Penemuan'), ('diagnosis', 'Diagnosis')], max_length=20)),
                ('bodySite', models.CharField(blank=True, max_length=245)),
                ('notes', models.TextField(blank=True)),
                ('id_pengguna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pengguna_condition_objects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(blank=True, choices=[('phone', 'Rumah'), ('fax', 'Kantor'), ('email', 'Sementara'), ('pager', 'Lama'), ('other', 'Lama')], help_text='Jenis sistem', max_length=10)),
                ('Value', models.CharField(blank=True, max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosticReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('registered', '<em></em> | '), ('partial', '<em></em> | '), ('final', '<em></em> | '), ('corrected', '<em></em> | '), ('appended', '<em></em> | '), ('cancelled', '<em></em> | '), ('entered-in-error', '<em></em> | ')], max_length=20)),
                ('category', models.CharField(blank=True, max_length=20)),
                ('code', models.CharField(max_length=20)),
                ('effectiveDateTime', models.DateTimeField()),
                ('issued', models.DateTimeField(default=django.utils.timezone.now)),
                ('conclusion', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.CharField(choices=[('inpatient', '<em>Rawat Inap</em> | '), ('outpatient', '<em>Rawat Jalan</em> | '), ('ambulatory', '<em></em> | '), ('emergency', '<em></em> | '), ('home', '<em>Rumah</em> | '), ('field', '<em>Lapangan</em> | '), ('daytime', '<em></em> | '), ('virtual', '<em>Virtual</em> | '), ('other', '<em>Lainnya</em> | ')], max_length=15)),
                ('reason', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=20)),
                ('detail', models.TextField(blank=True)),
                ('condition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Condition')),
            ],
        ),
        migrations.CreateModel(
            name='HealthcareService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceCategory', models.CharField(blank=True, max_length=20)),
                ('serviceName', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HumanName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Nama Lengkap', max_length=245)),
                ('family', models.CharField(help_text='Nama keluarga', max_length=50)),
                ('given', models.CharField(help_text='Nama pemberian/nama depan termasuk nama tengah (jika ada)', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('Type', models.CharField(choices=[('UDI', 'Universal Device Identifier'), ('SNO', 'Serial Number'), ('SB', 'Social Beneficiary Identifier'), ('PLAC', 'Placer Identifier'), ('FILL', 'Filler Identifier'), ('KTP', 'KTP'), ('DL', 'Surat Izin Mengemudi'), ('PPN', 'Nomor Paspor'), ('EN', 'Employer number'), ('MD', 'Medical License number'), ('DR', 'Donor Registration Number')], max_length=100)),
                ('Value', models.CharField(max_length=65, primary_key=True, serialize=False)),
                ('condition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Condition')),
                ('diagnosticreport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.DiagnosticReport')),
                ('encounter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Encounter')),
                ('healthcareservice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.HealthcareService')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('description', models.TextField(blank=True, help_text='Deskripsi lokasi')),
            ],
        ),
        migrations.CreateModel(
            name='pasien_dari_dokter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_edit', models.BooleanField(default=False)),
                ('status_sinkronisasi', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=True, help_text='Apakah rekam medis pasien masih aktif?', verbose_name='Aktif')),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'Laki-laki'), ('FEMALE', 'Perempuan'), ('OTHER', 'lainnya'), ('UNKNOWN', 'Tidak Diketahui')], max_length=10, verbose_name='Jenis Kelamin')),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('deceasedBoolean', models.BooleanField()),
                ('deceasedDateTime', models.DateTimeField(blank=True, null=True)),
                ('maritalStatus', models.CharField(blank=True, choices=[('DIVORCED', 'Bercerai'), ('MARRIED', 'Menikah'), ('NEVERMARRIED', 'Belum Menikah'), ('WIDOWED', 'Duda/Janda'), ('UNKNOWN', 'Tidak Diketahui')], max_length=20)),
                ('language', models.CharField(choices=[('id', 'Indonesia'), ('en', 'Inggris')], help_text='Bahasa yang dikuasai', max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(blank=True)),
                ('end', models.DateTimeField(blank=True)),
                ('DiagnosticReport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.DiagnosticReport')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Address')),
                ('condition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Condition')),
                ('contactpoint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.ContactPoint')),
                ('encounter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Encounter')),
                ('identifier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Identifier')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Practitioner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_edit', models.BooleanField(default=False)),
                ('status_sinkronisasi', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(blank=True, null=True)),
                ('id_pengguna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pengguna_practitioner_objects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PractitionerRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('doctor', 'Dokter'), ('nurse', 'Perawat'), ('pharmacist', 'Apoteker'), ('researcher', 'Peneliti'), ('teacher', 'Pengajar'), ('ict', 'Profesional ICT')], max_length=20)),
                ('specialty', models.CharField(blank=True, choices=[('cardio', 'Ahli Jantung'), ('dent', 'Dokter Gigi'), ('dietary', 'Konsultan Diet'), ('midw', 'Bidan'), ('sysarch', 'Ahli Sistem')], max_length=20)),
                ('practitioner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Practitioner')),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Value', models.DecimalField(blank=True, decimal_places=3, max_digits=60)),
                ('comparator', models.CharField(blank=True, choices=[('less', '<'), ('lessequal', '<='), ('moreequal', '>='), ('more', '>')], max_length=9)),
                ('unit', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.TextField(blank=True, default='')),
                ('display', models.CharField(blank=True, max_length=245)),
                ('condition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Condition')),
                ('diagnosticreport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.DiagnosticReport')),
                ('encounter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Encounter')),
                ('healthcareservice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.HealthcareService')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Location')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='rekmed_pasien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Condition')),
                ('pasien', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patientcondition', to='formdemografi.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=20)),
                ('healthcareservice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.HealthcareService')),
            ],
        ),
        migrations.CreateModel(
            name='statusDokterTersedia',
            fields=[
                ('SedangPraktek', models.CharField(blank=True, choices=[('off', 'Sedang tidak praktek'), ('on', 'Sedang praktek')], default=False, max_length=25, verbose_name='Status anda')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, primary_key=True, serialize=False)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tabel_sinkronisasi_client',
            fields=[
                ('status_edit', models.BooleanField(default=False)),
                ('status_sinkronisasi', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(blank=True, null=True)),
                ('id_transaksi_client', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('id_pengguna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pengguna_tabel_sinkronisasi_client_objects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tabel_sinkronisasi_cloud',
            fields=[
                ('id_transaksi_cloud', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date_received', models.DateTimeField(default=django.utils.timezone.now)),
                ('tbl_client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formdemografi.tabel_sinkronisasi_client')),
            ],
        ),
        migrations.AddField(
            model_name='period',
            name='practitioner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Practitioner'),
        ),
        migrations.AddField(
            model_name='period',
            name='practitionerrole',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.PractitionerRole'),
        ),
        migrations.AddField(
            model_name='patient',
            name='dokter',
            field=models.ManyToManyField(related_name='para_pasien', through='formdemografi.pasien_dari_dokter', to='formdemografi.Practitioner'),
        ),
        migrations.AddField(
            model_name='patient',
            name='id_pengguna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pengguna_patient_objects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pasien_dari_dokter',
            name='dokter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pasiendokter', to='formdemografi.Practitioner'),
        ),
        migrations.AddField(
            model_name='pasien_dari_dokter',
            name='pasien',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pasiendokter', to='formdemografi.Patient'),
        ),
        migrations.AddField(
            model_name='identifier',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Patient'),
        ),
        migrations.AddField(
            model_name='identifier',
            name='practitioner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Practitioner'),
        ),
        migrations.AddField(
            model_name='humanname',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Patient'),
        ),
        migrations.AddField(
            model_name='humanname',
            name='practitioner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Practitioner'),
        ),
        migrations.AddField(
            model_name='contactpoint',
            name='healthcareservice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.HealthcareService'),
        ),
        migrations.AddField(
            model_name='contactpoint',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Patient'),
        ),
        migrations.AddField(
            model_name='contactpoint',
            name='practitioner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Practitioner'),
        ),
        migrations.AddField(
            model_name='condition',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='formdemografi.Patient'),
        ),
        migrations.AddField(
            model_name='codeableconcept',
            name='diagnosticreport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.DiagnosticReport'),
        ),
        migrations.AddField(
            model_name='codeableconcept',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Patient'),
        ),
        migrations.AddField(
            model_name='codeableconcept',
            name='practitioner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Practitioner'),
        ),
        migrations.AddField(
            model_name='codeableconcept',
            name='practitionerrole',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.PractitionerRole'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='DiagnosticReport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.DiagnosticReport'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Patient'),
        ),
        migrations.AddField(
            model_name='antrian',
            name='dokter_tujuan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Practitioner'),
        ),
        migrations.AddField(
            model_name='address',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Patient'),
        ),
        migrations.AddField(
            model_name='address',
            name='practitioner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formdemografi.Practitioner'),
        ),
        migrations.AlterUniqueTogether(
            name='tabel_sinkronisasi_client',
            unique_together=set([('id_pengguna', 'id_transaksi_client')]),
        ),
    ]