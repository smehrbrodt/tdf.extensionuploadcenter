from plone import api
from tdf.extensionuploadcenter.eupcenter import IEUpCenter


def notifiyAboutNewVersion(eupproject, event):
    if hasattr(event, 'descriptions') and event.descriptions:
        for d in event.descriptions:
            if hasattr(d, 'interface') and d.interface is IEUpCenter and 'available_versions' in d.attributes:
                users = api.user.get_users()
                message = 'We added a new version of LibreOffice to the list.\n' \
                          'Please add this version to your LibreOffice extension release(s), ' \
                          'if it is (they are) compatible with this version.\n\n' \
                          'Kind regards,\n\n' \
                          'The LibreOffice Extension and Template Site Administration Team'
                for f in users:
                    mailaddress = f.getProperty('email')
                    api.portal.send_email(
                        recipient=mailaddress,
                        sender="noreply@libreoffice.org",
                        subject="New Version of LibreOffice Added",
                        body=message,
                    )
