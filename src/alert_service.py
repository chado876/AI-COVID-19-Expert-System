import dbUtil as dbUtil
from models.alert import Alert

def init_alerts():
    curr_alerts = dbUtil.get_alerts()
    
    if(len(curr_alerts) == 0):
        very_high_alert = Alert()
        very_high_alert.id = 0
        very_high_alert.value = 0 #initialize all alerts with 0 (will be ingored)
        very_high_alert.alert_type = "Very High Risk"

        high_alert = Alert()
        high_alert.id = 1
        high_alert.value = 0 #initialize all alerts with 0 (will be ingored)
        high_alert.alert_type = "High Risk"

        low_alert = Alert()
        low_alert.id = 2
        low_alert.value = 0 #initialize all alerts with 0 (will be ingored)
        low_alert.alert_type = "Low Risk"

        not_alert = Alert()
        not_alert.id = 3
        not_alert.value = 0 #initialize all alerts with 0 (will be ingored)
        not_alert.alert_type = "Not at Risk"

        dbUtil.add_alert(very_high_alert)
        dbUtil.add_alert(high_alert)
        dbUtil.add_alert(low_alert)
        dbUtil.add_alert(not_alert)

        print("DEFAULT ALERTS SEEDED SUCCESSFULLY")
    dbUtil.get_alerts()

def update_alert(alert_type,val):
    alert = Alert()
    alert.alert_type = alert_type
    alert.value = val
    dbUtil.update_alert(alert)

def get_alert_vals():
    alerts = dbUtil.get_alerts()
    alert_val_list = []

    for alert in alerts:
        alert_val_list.append(alert.value)

    return alert_val_list

# alert = Alert()
# alert.alert_type = "High Risk"
# alert.value = 0
# update_alert(alert)
# dbUtil.get_alerts()