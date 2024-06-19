import re,csv
 
API_ID   = 28421849 #api_id
CHAT_ID  = -1002118768399  #id chat donde se enviara
NUMERO   = '+18493121009'  #aqui el numero de celular de la cuenta
API_HASD = "72a558128d5899df66ec29f89ddb9eea" #api hasd
TOKEN    = "6846964757:AAGZcMEEAYMgUmfy4ACT00_E_-xk8AKQ-T4" #token del bot , recuerde que el bot debe estar agregado en el chat por el eñl enviara el tecto

DEAD = ['❌']


APROVED = [
' CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number.',
 'CCN CARD / CVV2 MISMATCH: 15004-THIS TRANSACTION CANNOT BE PROCESSED. PLEASE ENTER A VALID CREDIT CARD VERIFICATION NUMBER.',
 '𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: APPROVED',
 'AUTHENTICATE_SUCCESSFUL',
'[ᗎ] 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: SUCCEEDED',
'CVV2 MISMATCH',
 'CARD ISSUER DECLINED CVV',
 'YOUR ORDER HAS BEEN SUCCESSFULLY PROCESSED!',
 '[ CHARGED 0.01 ]',
'PROCESSOR DECLINED: APPROVED (1000)',
 'CHARGED $15.00',
 'NOT FUNDS \ TRANSACTION NORMAL - INSUFFICIENT FUNDS',
 'RESULT -» APPROVED',
 'SECURITY CODE WAS NOT MATCHED BY THE PROCESSOR',
 'THE BILLING ZIP CODE PROVIDED DOES NOT MATCH THE INFORMATION ON FILE WITH THE CARDHOLDER.',
 'SECURITY CODE WAS NOT MATCHED BY THE PROCESSOR',
 '2010: CARD ISSUER DECLINED CVV (C2 : CVV2 DECLINED)',
 'SUCCESSFUL ✅',
 '🝂 APPROVED!🟩 ',
 'GATEWAY REJECTED: AVS',
 '1000: APPROVED',
 'CARD ISSUER DECLINED CVV',
 'CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number.',
    'Approved Status code 2010: Card Issuer Declined CVV (C2 : CVV2 DECLINED)',
   '🟢 CVV Matched.',
    'CVC Declined | N7 : Decline for CVV2 failure',
    'Not Funds \ Transaction Normal - Insufficient Funds',
    'Charged $5.27',
    '2010: Card Issuer Declined CVV' ,
    "Your card's security code is incorrect.", 
    ' 𝑪𝒉𝒂𝒓𝒈𝒆𝒅 $𝟕 ✅',
    'Thank you for your purchase!',
    'N7 - CVV2 verification',
    'Decline for CVV2 failure',
    'The security code you entered does not match. Please update the CVV and try again. | fraud_security_code',
    'Payment Approved 0.1$ - is3DSecureRequired =>',
    '2010 Card Issuer Declined CVV',
    'INVALID_SECURITY_CODE',
    'avs_and_cvv: Gateway Rejected: avs_and_cvv',
    'CVV: [N] | AVS: [NNN]',
    '𝑪𝑽𝑪 -» unavailable - ⚜️ 𝑨𝑽𝑺 -» unavailable',
    'INVALID_BILLING_ADDRESS',
    '2001: Insufficient Funds (51 : DECLINED)',
    'Incorrect Cvc',
    'Card Issuer Declined CVV (2010)',
    '20051: Insufficient Funds',
    'C2 : CVV2 DECLINED',
    '[ APPROVED 🟩 ] ',
    'Charged',
    'Verified (85: NO REASN TO DECL) CVV: [M] | AVS: [XXN]',
    'cardCvv (INVALID_SECURITY_CODE)',
    'CVV2 Mismatch',
    'Security code was not matched by the processor',
    '1000: Approved',
    'AVS check failed CVV: N | AVS: N'
    'Not Funds \ Transaction Normal - Insufficient Funds',
    "Your card's security code is incorrect.",
    'Verified',
    ' 𝑪𝒉𝒂𝒓𝒈𝒆𝒅 9$ ✅',
    'The transaction has been declined because of an AVS mismatch. The address provided does not match billing address of cardholder.(27)',
    'credit card zip code mismatch',
    'succeeded',
    'Subscription Complete',
    'Gateway Rejected: avs!',
    '2001: Insufficient Funds (51 : DECLINED)',
    'Gateway Rejected: avs_and_cvv',
    '2001 Insufficient Funds',
    'Gateway Rejected: cvv',
     'you for your purchase!',
    'CVC Declined',

    'ErrorDeclinedInvalidCvv',

    'Verified',

    '2010: Card Issuer Declined CVV (C2 : CVV2 DECLINED)',

    'cardCvv (INVALID_SECURITY_CODE)',

    'Charged 0.01$ [Receipt]',

    'AVS check failed',

    'DCARDREFUSED:211:CVV2 DECLINED',

    'avs: Gateway Rejected: avs',

    "Error: Your card's security code is incorrect.",

    "The card's security code is incorrect.",

    '$ 3,18 ',


    '𝒔𝒕𝒂𝒕𝒖𝒔 = 𝒔𝒖𝒄𝒄𝒆𝒆𝒅𝒆𝒅 ',

    'CVV2 Mismatch',
    '⚜️ 𝑪𝑽𝑪 -» N - ⚜️ 𝑨𝑽𝑺 -» U',

    'Invalid Security Code!  Please Correct Security Code.',


    'Transaction declined.14002 - Transaction failed  because of payment processing failure.: 531 - The security code entered is invalid. Please check number and enter again',

    'CCN CARD / Security code was not matched by the processor',

    'CCN CARD / CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number.',

    'CVV2 DECLINED',

    'Processor declined: Approved (1000)',

    'The payment gateway declined the transaction because the security code (CVV) or expiration date did not match | recurly_the_security_code_you_entered_does_not_match',

    'Verified: 10574-This card authorization verification is not a payment transaction.',
    'AVS: [XXN] | CVV: [P]',

    'Transaction declined.301 - CVV Note: No Match',

    'Transaction declined.352 - CVV Note: No Match',

    'Transaction declined.218 - CVV Note: No Match',

    'Charged $14',

    'Order Placed | Charged $12',

    'AVS validation failed',

    'CVV2 Mismatch',

    'acct_stripe_card_incorrect_cvc',

    '2001: Insufficient Funds (51)',
        
    ]


def scrapp_ccs(text):

    if "|" in text:
        x = re.findall(r'\d+', text)

        if len(x[0]) < 16 :
            x.remove(x[0])
            if len(x) == 0:
                print(f'[⌁] - No Detectada ❌')
                return
            if len(x) == 1:
                print(f'[⌁] - No Detectada ❌')
                return
            elif len(x) == 2:
                print(f'[⌁] - Incomplet ccs ❌')
                return
            elif len(x) == 3:
                print(f'[⌁] - CVV Incomplet ❌')
                return
            cc = x[0]
            mm = x[1]
            yy = x[2]
            cvv = x[3]
            if len(cc) > 16:
                return
            if len(mm) > 2:
                return
            if len(yy) > 4:
                return
            if len(cvv) > 4:
                return

            if mm.startswith('2'):
                mm, yy = yy, mm
            if len(mm) >= 3:
                mm, yy, cvv = yy, cvv, mm
            if len(cc) < 15 or len(cc) > 16:
                print(f'[⌁] - Invalid Ccs ❌')
                return
            if len(yy) == 2:
                yy = '20'+yy

        
            return f'<code>{cc}|{mm}|{yy}|{cvv}</code>'
        else:
            
            if len(x) == 0:
                print(f'[⌁] - No Detectada ❌')
                return
            if len(x) == 1:
                print(f'[⌁] - No Detectada ❌')
                return
            elif len(x) == 2:
                print(f'[⌁] - Incomplet ccs ❌')
                return
            elif len(x) == 3:
                print(f'[⌁] - CVV Incomplet ❌')
                return
            cc = x[0]
            mm = x[1]
            yy = x[2]
            cvv = x[3]
            if len(cc) > 16:
                return
            if len(mm) > 2:
                return
            if len(yy) > 4:
                return
            if len(cvv) > 4:
                return

            if mm.startswith('2'):
                mm, yy = yy, mm
            if len(mm) >= 3:
                mm, yy, cvv = yy, cvv, mm
            if len(cc) < 15 or len(cc) > 16:
                print(f'[⌁] - Invalid Ccs ❌')
                return
            if len(yy) == 2:
                yy = '20'+yy

            return f'<code>{cc}|{mm}|{yy}|{cvv}</code>'
   



def get_bin_info(target_bin):
    bin = target_bin[:6]
    with open('binlist.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            bin_start_number = row.get('number', '')
            bin_start_brand = row.get('brand', '')
            
            if bin_start_number and bin_start_number.startswith(bin):

                return {
                    'level': row.get('level', ''),
                    'brand': bin_start_brand,
                    'type': row.get('type', ''),
                    'country': row.get('country', ''),
                    'bank': row.get('bank', ''),
                    'number': bin_start_number,
                    'flag': row.get('flag', ''),
                    'vendor': row.get('vendor', ''),
                    'bank_city': row.get('bank_city', '')
                }
            
            if bin_start_brand and bin_start_brand.startswith(bin):

                return {
                    'level': row.get('level', ''),
                    'brand': bin_start_brand,
                    'type': row.get('type', ''),
                    'country': row.get('country', ''),
                    'bank': row.get('bank', ''),
                    'number': row.get('number', ''),
                    'flag': row.get('flag', ''), 
                    'vendor': row.get('vendor', ''),
                    'bank_city': row.get('bank_city','')
                }

    
    return None


def getcards(text):
    card_info = re.search(r'(\d{15,16})+?[^0-9]+?(\d{1,2})[\D]*?(\d{2,4})[^0-9]+?(\d{3,4})', text)
    if card_info:
        cc, mes, ano, cvv = card_info.groups()
        cc = cc.replace("-", "").replace(" ", "")

        return [cc, mes, ano, cvv]
    
    return False
