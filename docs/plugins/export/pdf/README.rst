PDF plugin
===========

Description
-----------

This plugin adds the possibility to export a rendered page to a PDF file.

Activation
----------

Provide the `--plugin.export.pdf` option to the CLI.

Options
-------

+--------------+----------------------------------------+----------+---------+
| Option       | Description                            | Required | Default |
+==============+========================================+==========+=========+
| --pdf-file   | The path to the PDF file to generate.  | Yes      | `-`     |
+--------------+----------------------------------------+----------+---------+
| --pdf-option | A wkhtmltopdf_ option under the form   | No       | `-`     |
|              | "key=value". This option can be passed |          |         |
|              | multiple times. See the complete list  |          |         |
|              | of options here_.                      |          |         |
+--------------+----------------------------------------+----------+---------+

.. _wkhtmltopdf: https://wkhtmltopdf.org/
.. _here: https://wkhtmltopdf.org/usage/wkhtmltopdf.txt
