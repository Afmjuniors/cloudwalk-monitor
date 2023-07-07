class TransactionBusiness:
    def __init__(self):
        pass

    def _analyze_transactions(self,
                              total_transactios,
                              total_failed,
                              total_denied,
                              total_reversed,
                              total_processing
                              ):

        threshold_denied = .5
        threshold_reversed = .5
        threshold_failed = .5
        threshold_processing = .5

        if total_reversed / total_transactios >= threshold_reversed:
            self._send_alert('Number of reversed operations exceed the threshold')

        if total_denied / total_transactios >= threshold_denied:
            self._send_alert('Number of denied operations exceed the threshold')

        if total_failed / total_transactios >= threshold_failed:
            self._send_alert('Number of failed operations exceed the threshold')

        if total_processing / total_transactios >= threshold_processing:
            self._send_alert('Number of processing operations exceed the threshold')

    def _send_alert(self, message):
        print(f'Alert:{message}')

    def transaction_business(self, df):
        total_transactios = 0
        total_failed = 0
        total_denied = 0
        total_reversed = 0
        total_aprroved = 0
        total_processing = 0

        for index, row in df.iterrows():
            if row['status'] == 'failed':
                total_failed = row['count']
            elif row['status'] == 'denied':
                total_denied = row['count']
            elif row['status'] == 'reversed' or row['status'] == 'backend_reversed':
                total_reversed += row['count']
            elif row['status'] == 'approved' or row['status'] == 'refunded':
                total_aprroved += row['count']
            else:
                total_processing += row['count']

            total_transactios += row['count']

        self._analyze_transactions(total_transactios, total_failed, total_denied, total_reversed, total_processing)

