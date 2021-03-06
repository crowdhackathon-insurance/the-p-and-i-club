from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.template import loader

from clients.models import Client
from clients.models import ProposalFormSubmission
from clients.models import ProposalFormSubmissionField
from companies.models import ProposalForm
from companies.models import ProposalFormField


gpg = settings.GPG


def display_proposal_form(request, proposal_form_id):
    if request.method == 'POST':
        client = Client.objects.get(id=int(request.POST['client']))
        proposal_form = ProposalForm.objects.get(id=proposal_form_id)
        submission = ProposalFormSubmission.objects.create(
            client=client,
            proposal_form=proposal_form
        )
        fields = ProposalFormField.objects.filter(
            proposal_form=proposal_form
        )
        for field in fields:
            ProposalFormSubmissionField.objects.create(
                proposal_form_submission=submission,
                field=field,
                value=request.POST['%s' % field.id]
            )
        submission.plain_txt = loader.render_to_string(
            'brokers/proposal_form_submission.txt',
            {
                'proposal_form_submission': submission,
                'fields': ProposalFormSubmissionField.objects.filter(
                    proposal_form_submission=submission
                )
            }
        )

        signature = gpg.sign(
            submission.plain_txt,
            default_key=client.key_id,
            passphrase=request.POST['passphrase']
        )
        if signature.data == '':
            raise Exception(
                'Could not sign document! Error: %s' % signature.status
            )
        submission.plain_txt_signed = signature.data
        submission.save()
        response = redirect(
            display_proposal_form_submission, submission_id=submission.id
        )
        return response
    else:
        proposal_form = ProposalForm.objects.get(id=proposal_form_id)
        data = {
            'proposal_form': proposal_form,
            'fields': ProposalFormField.objects.filter(
                proposal_form=proposal_form
            ),
            'clients': Client.objects.all()
        }
        return render(request, 'brokers/proposal_form.html', data)

def display_proposal_form_submission(request, submission_id):
    submission = ProposalFormSubmission.objects.get(id=submission_id)
    data = {
        'proposal_form_submission': submission,
        'fields': ProposalFormSubmissionField.objects.filter(
            proposal_form_submission=submission
        )
    }
    return render(request, 'brokers/proposal_form_submission.html', data)

def display_proposal_form_submission_txt(request, submission_id):
    submission = ProposalFormSubmission.objects.get(id=submission_id)
    return HttpResponse(submission.plain_txt, content_type='text/plain; charset=utf-8')
