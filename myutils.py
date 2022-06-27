import io
import pandas as pd
import base64

from ipywidgets import HTML
from IPython.display import display

def dfs_to_excel(list_df, filename):
    # create a buffer to output the result
    output = io.BytesIO()

    # use the BytesIO object as the file handle
    writer = pd.ExcelWriter(output, engine='xlsxwriter')

    for n, tab in enumerate(list_df):
        tab.to_excel(writer,'sheet%s' % n)

    writer.save()
    
    b64 = base64.b64encode(output.getbuffer().tobytes())
    payload = b64.decode()

    html_buttons = '''<html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    <a download="{filename}" href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{payload}" download>
    <button class="p-Widget jupyter-widgets jupyter-button widget-button mod-warning">Download Excel</button>
    </a>
    </body>
    </html>
    '''
    
    html_button = html_buttons.format(payload=payload,filename=filename)
    display(HTML(html_button))
