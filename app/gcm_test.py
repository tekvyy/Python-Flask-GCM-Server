__author__ = 'tekvy'
from flask import Flask
from flask_gcm import GCMAuthenticationError
import json
from flask_gcm import JSONMessage

app = Flask(__name__)

from flask.ext.gcm import GCM

API_KEY = "AIzaSyAdBg_UiD4aheNB0sjTwjWKtORzkIPkoeI"
gcm = GCM()
app.config['GCM_KEY'] = API_KEY
gcm.init_app(app)



# multicast = JSONMessage(["APA91bFsP-Lv-e_Umy74f1yZ0MZXywGNStJ8n8UdsAwixaIGF1ILjSuVV8yyoGw3jTDSo-eTv1G63nyQ5rV-IgsbaLU_SdCR1QiqW-kWZ___Kcq_b-ZbWC3AzMHpDODZMMX8zmK_clGZPfrA9yWcDITNwi0hJG_DqQ"], data, collapse_key='my.key', dry_run=False)

def send_gcm_notif(gcm_regid, value1, value2):

    data = {'header': value1, 'content': value2}
    multicast = JSONMessage([gcm_regid], data, collapse_key='my.key', dry_run=False)

    try:
    # attempt send
        res_multicast = gcm.send(multicast)

        for res in [res_multicast]:
            # nothing to do on success
            for reg_id, msg_id in res.success.items():
                print "Successfully sent %s as %s" % (reg_id, msg_id)

    # update your registration ID's
        for reg_id, new_reg_id in res.canonical.items():
            print "Replacing %s with %s in database" % (reg_id, new_reg_id)

    # probably app was uninstalled
        for reg_id in res.not_registered:
            print "Removing %s from database" % reg_id

    # unrecoverably failed, these ID's will not be retried
    # consult GCM manual for all error codes
        for reg_id, err_code in res.failed.items():
            print "Removing %s because %s" % (reg_id, err_code)

    # if some registration ID's have recoverably failed
        if res.needs_retry():
            # construct new message with only failed regids
            retry_msg = res.retry()
        # you have to wait before attempting again. delay()
        # will tell you how long to wait depending on your
        # current retry counter, starting from 0.
            print "Wait or schedule task after %s seconds" % res.delay(retry)
        # retry += 1 and send retry_msg again

    except GCMAuthenticationError:

    #stop and fix your settings
        print "Your Google API key is rejected"

    except Exception:
    # your network is down or maybe proxy settings
    # are broken. when problem is resolved, you can
    # retry the whole message.
        print "Something wrong with requests library"