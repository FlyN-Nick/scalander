# Generated by Django 4.0 on 2022-10-12 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_user_email_meetingtimeproposal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commitment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_app.user'),
        ),
        migrations.AlterField(
            model_name='meetingproposalattendance',
            name='proposal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_app.meetingtimeproposal'),
        ),
        migrations.AlterField(
            model_name='meetingproposalattendance',
            name='user_subscription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_app.usermeetingsubscription'),
        ),
        migrations.AlterField(
            model_name='meetingtimeproposal',
            name='meeting',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_app.meeting'),
        ),
        migrations.AlterField(
            model_name='usermeetingsubscription',
            name='meeting',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_app.meeting'),
        ),
        migrations.AlterField(
            model_name='usermeetingsubscription',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_app.user'),
        ),
    ]
