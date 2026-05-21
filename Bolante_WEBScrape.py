from __future__ import annotations

import csv
from datetime import datetime, timedelta
import requests

# =========================================================
# STARLINK API CONFIG
# =========================================================

ACCOUNT_ID = "ACC-2735603-74738-20"
SERVICE_LINE_ID = "AST-2293597-46342-54"

# Replace with your current token
ACCESS_TOKEN = "CfDJ8B0rUwu9drZBtlp6Z3PrbGWcZTRJ1k68CFQZttju-3FpSbEYyspw1YdEYL2TQfz7W1iaJeR233BG4Dvg147lXgxkANniqx3Q7p7jYpAGZX1sLcvRi5E6k3Nuz6O9WBQhDzq4KQh81-so8vg0xOnj0MHiHZlpjMJ_SCuFuGCxoWTvvwtbiU1aWIyNfLUKmPmMtLppiNx1jltrtgbRyNQzppnfSRgj2rhMxJt8CtSwPqSf9t3n1InO3M4WP5zekevyhwZyQWLsY_mJRSbWoEPzk8TIP8p5N_wONJxOVQC4ZUf0TKMM27t5p_Y-a0FbsDdfZz6Wc6JgcTgpQP2lD-sN-KGhOmh_B5sKhPci_hn3f6IUTVxveR-1V5ylzcok7Ny3XoRTJxh5jDrMWUYU5ve-2oZCgG5j1x_rvx3bkvkAszAYCfL5xXwMHpZz0t2Eh68_UFS3g-A0EhRAY7UwTa_Dr6hsdEbk7x6_s-VqWEG690X67q4QoJSG586cTfEbJihasQAD1Nnia2YXAu9euNdhzFanUAFBKLVKViqfwSeKKcLIEwbeI8-TdgghAYOv3sostcJo-L81Wn0eesuvxotL3dRh04ijZAhCWtE_t1_89whCYb_v32DJr25b_SgZfnh_BpSBf8ePQsfk2wa4a5PwfUwmE9gB3458KjJQl5msUeUQSgNyfXWJd2jFOE6-gdoweCl_xutgMZfOfXNvmjatd0Tq4522k1y4MMrbdDuJCUvWfxanZs1fnO7qzkdhx4Dp-DQQzLLPsNiW3MYPvgGWYT6Bg_ZCv1HD0aOYXW_iIxKmmP52ttIgB1jPsN6Gd_-Jb9VUx-Jkvlk3zpJP3NHP1UceZXvZrSVVpoUnHrvEMjrAXAp54YVPOaF87Yh0pZ4zX9N7ki5kRmKNgObCMqZjDjsQ50dYwkdWa1t36t_gzrdh_ULUyavpzxjRBVRACI33eg0RSHwLJGV9Jk_13XioornRpANa1i_Ts3peAeFih-MC7IaCYsgi2sB1cnzyrfO2Og7k-bvBbIMJYfrxVuV1yZWdWOFzYhFfMN2DCoQBYtdoD-gyq2CD-lJtbPir7ufw4s3dusWNWL6nmrVB2RP50LnuDyQbYC4Gfs1cvapSRbz9XM0Xi8QV9j5MYpt8-X7DBaw14zQbkdMWt67X4FvAbq3GHziN806ABJZx0U6Jbdjh86RxY6ola_9aYuIg4AlP755Y3Y-3XhOdgi7d_CQfBcdPsBuCov6dhdKiTq_8cCWO-rMlLEEPdfdNvfOHpegrw-gBMfrjX_Kc2pAsXeVs2RrobPoPdiTv7x8UdNBkF6ZjONN1R6SMvF8fXbL3Ne5PYRWvjq3DD41lSECEhv-wsurdGiK5DASjQNR2YglZvg5H8NHW8atxq_eAW55vCah88SHaGVALVslikuUxD1sJYsJKOWfUA_QlJHoaQrQlNbJx8jiV2-nV4yopngApuuAIUWd10LXwGlkiUY2JRifNsNnoG9U3ccgPbtKngzpMkraQjKRslBVb7vJ5vxgzq2T_zSx2-Pa7VOSGdGv3EM68xypnOwp3KozyDBwiJGfcRH_raO5yqBnBnITwP84DH9khMiRdMf8IE2Ss08MCs5gQc_3Owbu5negvc6Is8qf8FM3vhrtDctkJC3qF5kXzwPXQE6AN5kaLOCerMnl42ZBzSYshcl-qzOUPuDtAr2CPSWs_hPZk-b8_B-PdYvRvJVgmW5lugoFdzYDKpC2b3qkuBp8uTR6bKSPwTCviF7mAvHFcrOZNDKVbAYTObkwzagcjXLcNm6KaXqOHvC9-0MtlnljXdzFJr7SAVT8e3Ind0uoNuSWV6m6nnWn6I_O3O0HPw3DdnGWYgdxESK__EQo-Byx6n8kuE_YDi1PQMYYOS5_140a8rFhIOdIgIcLQ0yiaGXTQNzlx6z08dgQfWJAZGT_ZhbZfhJ2Ga7ogflxozGof2XdxKAf68bLduefcCgbrcQoC38cTACpy4Vy9Jgvh7QWMByR2NMEKKWxpGDzEjTOhVErVK-m4ye09sn7qABXdEnK1lxAfkt_h6CKg1ZcsGzxCYYgthZ2qOduwZvdDFSdl6P5OwL7G5nn6XwB5AnwQSN55CPzBQH8LcSD19suq0yzAshRZ1SuHLT6uRpR1KJqNhIDo5sEMeAqoI234npXmUOHF47gkTRFW30Dl2IxLpiyFA-lxVNsouvSsVPI7ZWGYQiyVJiEPjnk0ANIAG-iiH0MiMh7iYdvPjOIAZNqUaoLqxEG1KX0xUgHOlawK7Kwph8gp5XDLtScAAlvGmzt9pMPSqpWWHtahNY7U6z-H_ELp-z3nJaq1Nal1xsrdp65MQSZMUo-A6xcxk-1q3CoW2zhfxkU_luZcJzxa0jgz_MSj_rOKXm2hxDj2b2B2s4qvJ0WHHYik0DvbIc_tyKR3Lgrn9NBSJ2q_YcUA1e7H5r_45MaoTDcJNsUgW3yVPq4OxmXOb1NPC815V8-51Nvwo4eOVSfvf8ap1KKRWiKijKVwHoaRgUsP84RUS64vbdo4fKxlZK5uGKBF6YzXJOqvnqolnBlK-mTLytyB0FfpiRLATFLO7fTHyvq5Wwzo97j0M5AMwE81Pw_q97Uz9eFYyDKh62WUKrwVj-3518kO2tMiHfn-WKbHemn30rNZVf0wd2Dw2aldr0sdbA5uo-u4JO-_yyRX0gDC5GQlZDYslXMBUQojBbisu737RFbMLrHCMtoNcT8MIN_H2IDD7Qe8O3tYi_RGia4rZ5bz3GDZ3KfZaFgA9IItWw37ghu3AN9KBuCwhAzBe76o_-eeAW6n7N1laz9rALokiWyxaugl4ejQqpRCGLfb_G3ZY6yO86hLCNLH2sLHcb9Wt54XOyvHrnrKnghznn2RESQtSOYY3wcdiNttOTdJnB4ACNZZK55M8q1CelWyJbhx70EuDAJCjjwMz5k3ZDT9rBdyfN0KaBr1VZgU2r8A3ZJf12NCvdVdTlE1qsVU5JP2E1IDcEpsZgUMpJW6ghBhltQE6AxYZw1ql9PZstAbXio9fiZCTZbGvRf3s_2k6gE2xVblk4QFS4cg3K5rpHbCw5ecIXTPjEGP2nDivMTltYJ1QmeSruYFltLpBoktnkQt7SrHzunrRRWjV0MNk4my_DzNE2UnuRKwF5BuL7O96rzPs8Z_3KN6iKR--fHFyTpI707sZ_V7NQ"

# Select month to export
# Format: YYYY-MM
SELECTED_MONTH = "2026-05"

# Output CSV filename
OUTPUT_FILE = f"Sir_Val's_Starlink_Usage_{SELECTED_MONTH}.csv"

# =========================================================
# API REQUEST
# =========================================================

url = (
    f"https://starlink.com/api/telemetryagg/v1/"
    f"data-usage/account/{ACCOUNT_ID}/"
    f"service-line/{SERVICE_LINE_ID}/annotated"
)

session = requests.Session()

session.cookies.update({
    "Starlink.Com.Access.V1": ACCESS_TOKEN
})

response = session.get(url)

# Check request status
if response.status_code != 200:
    raise Exception(
        f"Request failed!\n"
        f"Status Code: {response.status_code}\n"
        f"Response: {response.text}"
    )

data = response.json()

# =========================================================
# EXTRACT DAILY DATA
# =========================================================

billing_cycles = data["content"]["billingCyclesAnnotated"]

rows = []

for cycle in billing_cycles:

    start_date_str = cycle["startDate"][:10]

    start_date = datetime.strptime(
        start_date_str,
        "%Y-%m-%d"
    )

    daily_data = cycle["dailyData"]

    for i, entry in enumerate(daily_data):

        current_date = start_date + timedelta(days=i)

        current_month = current_date.strftime("%Y-%m")

        # Filter selected month only
        if current_month != SELECTED_MONTH:
            continue

        usage_gb = round(float(entry[0]), 2)

        rows.append([
            current_date.strftime("%Y-%m-%d"),
            usage_gb
        ])

# =========================================================
# SAVE CSV
# =========================================================

if not rows:
    print(f"No data found for month: {SELECTED_MONTH}")

else:
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["date", "usage_gb"])

        writer.writerows(rows)

    print(f"Successfully exported {len(rows)} records!")
    print(f"CSV file saved as: {OUTPUT_FILE}")