# ferramentas utilizadas
"""
Kaggle para obter os dados, 
AWS IAM para criar usuário, 
AWS CLI para encaminhar dados ao bucket S3,
S3 para armazenar no formato Data Lake, 
Glue Crawler para extrair os dados do s3, 
GLue para realizar o ETL, 
Athena para consultar os dados,
Houve um erro por causa dos dados terem um formato diferente do padrão aws e com isso precisaremos formatar, 
Lambda para criar uma função que irá editar o .csv,



"""



# processo end to end AWS #
usuario = 'usuario_default'
senha_console = '027032nN@'
url_console = 'https://851725466213.signin.aws.amazon.com/console'
chave_acesso = 'AKIA4MTWLHJSQJDU6AYG'
chave_acesso_secreta = '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'
bucket_s3 = 'projeto-0'
enviar_dados_s3_json = 'aws s3 cp . s3://projeto-0/home/vm1/Documentos/VS_CODE/Estudos/Portifólio_Projeto-1/dados-YT --recursive --exclude "*" --include "*.json"'
enviar_dados_s3_csv = (
"""
aws s3 cp CAvideos.csv s3://projeto-0/home/vm1/Documentos/VS_CODE/Estudos/Portifólio_Projeto-1/dados-YT/
aws s3 cp DEvideos.csv s3://projeto-0/home/vm1/Documentos/VS_CODE/Estudos/Portifólio_Projeto-1/dados-YT/
aws s3 cp FRvideos.csv s3://projeto-0/home/vm1/Documentos/VS_CODE/Estudos/Portifólio_Projeto-1/dados-YT/
aws s3 cp GBvideos.csv s3://projeto-0/home/vm1/Documentos/VS_CODE/Estudos/Portifólio_Projeto-1/dados-YT/
aws s3 cp INvideos.csv s3://projeto-0/home/vm1/Documentos/VS_CODE/Estudos/Portifólio_Projeto-1/dados-YT/
aws s3 cp JPvideos.csv s3://projeto-0/home/vm1/Documentos/VS_CODE/Estudos/Portifólio_Projeto-1/dados-YT/
aws s3 cp KRvideos.csv s3://projeto-0/home/vm1/Documentos/VS_CODE/Estudos/Portifólio_Projeto-1/dados-YT/
aws s3 cp MXvideos.csv s3://projeto-0/home/vm1/Documentos/VS_CODE/Estudos/Portifólio_Projeto-1/dados-YT/ 
aws s3 cp RUvideos.csv s3://projeto-0/home/vm1/Documentos/VS_CODE/Estudos/Portifólio_Projeto-1/dados-YT/
aws s3 cp USvideos.csv s3://projeto-0/home/vm1/Documentos/VS_CODE/Estudos/Portifólio_Projeto-1/dados-YT/

""")