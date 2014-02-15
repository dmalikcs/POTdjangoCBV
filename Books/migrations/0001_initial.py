# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Publisher'
        db.create_table(u'Books_publisher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('state_province', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=30)),
        ))
        db.send_create_signal(u'Books', ['Publisher'])

        # Adding model 'Author'
        db.create_table(u'Books_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('salutation', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('headshot', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'Books', ['Author'])

        # Adding model 'Book'
        db.create_table(u'Books_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Books.Publisher'])),
            ('publication_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'Books', ['Book'])

        # Adding M2M table for field authors on 'Book'
        db.create_table(u'Books_book_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'Books.book'], null=False)),
            ('author', models.ForeignKey(orm[u'Books.author'], null=False))
        ))
        db.create_unique(u'Books_book_authors', ['book_id', 'author_id'])


    def backwards(self, orm):
        # Deleting model 'Publisher'
        db.delete_table(u'Books_publisher')

        # Deleting model 'Author'
        db.delete_table(u'Books_author')

        # Deleting model 'Book'
        db.delete_table(u'Books_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table('Books_book_authors')


    models = {
        u'Books.author': {
            'Meta': {'object_name': 'Author'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'headshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'salutation': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'Books.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Books.Author']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Books.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'Books.publisher': {
            'Meta': {'ordering': "['-name']", 'object_name': 'Publisher'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'state_province': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '30'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['Books']