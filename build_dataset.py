import csv
import sys
import re
from pprint import pprint
from pathlib import Path

string = '''

### LOVD-version 3000-29b ### Full data download ### To import, do not remove or alter this header ###
## Filter: (gene_public = TAS2R38)
# charset = UTF-8

## Genes ## Do not remove or alter this header ##
## Count = 1
"{{id}}"	"{{name}}"	"{{chromosome}}"	"{{chrom_band}}"	"{{imprinting}}"	"{{refseq_genomic}}"	"{{refseq_UD}}"	"{{reference}}"	"{{url_homepage}}"	"{{url_external}}"	"{{allow_download}}"	"{{id_hgnc}}"	"{{id_entrez}}"	"{{id_omim}}"	"{{show_hgmd}}"	"{{show_genecards}}"	"{{show_genetests}}"	"{{show_orphanet}}"	"{{note_index}}"	"{{note_listing}}"	"{{refseq}}"	"{{refseq_url}}"	"{{disclaimer}}"	"{{disclaimer_text}}"	"{{header}}"	"{{header_align}}"	"{{footer}}"	"{{footer_align}}"	"{{created_by}}"	"{{created_date}}"	"{{edited_by}}"	"{{edited_date}}"	"{{updated_by}}"	"{{updated_date}}"
"TAS2R38"	"taste receptor, type 2, member 38"	"7"	"q34"	"no"	"NG_016141.1"	"UD_132118988987"	""	"http://www.LOVD.nl/TAS2R38"	""	"1"	"9584"	"5726"	"607751"	"1"	"1"	"1"	"1"	"Establishment of this gene variant database (LSDB) was supported by the <a href=\'http://www.LUMC.nl\' target=\'_blank\'>Leiden University Medical Center (LUMC)</a>, Leiden, Nederland."	""	"g"	"http://databases.lovd.nl/shared/refseq/TAS2R38_codingDNA.html"	"1"	""	""	"-1"	""	"-1"	"00001"	"2010-04-29 00:00:00"	"00006"	"2016-08-08 09:19:51"	"00006"	"2020-06-05 17:29:26"


## Transcripts ## Do not remove or alter this header ##
## Count = 1
"{{id}}"	"{{geneid}}"	"{{name}}"	"{{id_mutalyzer}}"	"{{id_ncbi}}"	"{{id_ensembl}}"	"{{id_protein_ncbi}}"	"{{id_protein_ensembl}}"	"{{id_protein_uniprot}}"	"{{remarks}}"	"{{position_c_mrna_start}}"	"{{position_c_mrna_end}}"	"{{position_c_cds_end}}"	"{{position_g_mrna_start}}"	"{{position_g_mrna_end}}"	"{{created_by}}"	"{{created_date}}"	"{{edited_by}}"	"{{edited_date}}"
"00020774"	"TAS2R38"	"taste receptor, type 2, member 38"	"001"	"NM_176817.4"	""	"NP_789787.4"	""	""	""	"-84"	"1059"	"1002"	"141673573"	"141672431"	""	"0000-00-00 00:00:00"	""	""


## Diseases ## Do not remove or alter this header ##
## Count = 3
"{{id}}"	"{{symbol}}"	"{{name}}"	"{{inheritance}}"	"{{id_omim}}"	"{{tissues}}"	"{{features}}"	"{{remarks}}"	"{{created_by}}"	"{{created_date}}"	"{{edited_by}}"	"{{edited_date}}"
"00000"	"Healthy/Control"	"Healthy individual / control"	""	""	""	""	""	"00000"	"2012-07-26 17:29:43"	""	""
"00198"	"?"	"unclassified / mixed"	""	""	""	""	""	"00006"	"2013-09-13 14:21:47"	"00006"	"2016-10-22 17:54:40"
"01502"	"THIOT"	"tasting, henylthiocarbamide (bitter)"	"AD"	"171200"	""	""	""	"00006"	"2014-09-25 23:29:40"	"00006"	"2021-12-10 21:51:32"


## Genes_To_Disesaes ## Do not remove or alter this header ##
## Count = 1
"{{geneid}}"	"{{diseaseid}}"
"TAS2R38"	"01502"

'''

def load_data(file_path):
    data = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def parse(string):
    data = []
    for line in string.splitlines():
        if line.startswith('## ') and line.endswith('header ##'):
            block = line

def main():
    data = parse(string)
    pprint(data)

if __name__ == '__main__':
    main()