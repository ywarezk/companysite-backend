# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Workers'
        db.create_table(u'companysite_backend_app_workers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 6, 0, 0))),
            ('modified_data', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 6, 0, 0), auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True, blank=True)),
            ('html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'companysite_backend_app', ['Workers'])


    def backwards(self, orm):
        # Deleting model 'Workers'
        db.delete_table(u'companysite_backend_app_workers')


    models = {
        u'companysite_backend_app.flatpage': {
            'Meta': {'object_name': 'Flatpage'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 6, 0, 0)'}),
            'html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_data': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 6, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        },
        u'companysite_backend_app.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 6, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified_data': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 6, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'technologies': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'companysite_backend_app.workers': {
            'Meta': {'object_name': 'Workers'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 6, 0, 0)'}),
            'html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified_data': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 8, 6, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['companysite_backend_app']