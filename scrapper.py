import requests
from bs4 import BeautifulSoup

def scrap_infojobs():
    url = 'https://www.infojobs.net/jobsearch/search-results/list.xhtml?keyword=desarrollad&normalizedJobTitleIds=&provinceIds=&cityIds=&teleworkingIds=2&categoryIds=&workdayIds=&educationIds=&segmentId=&contractTypeIds=&page=1&sortBy=RELEVANCE&onlyForeignCountry=false&countryIds=&sinceDate=ANY&subcategoryIds='
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    job_elements = soup.find_all('div', class_='ij-OfferList-row')

    for job_element in job_elements:
        title = job_element.find('h2', class_='ij-OfferCardContent-description-title').text.strip()
        company = job_element.find('a', class_='ij-OfferCardContent-description-subtitle').text.strip()
        location = job_element.find('li', class_='ij-OfferCardContent-description-list').text.strip()
        print(f'Título: {title}\nEmpresa: {company}\nUbicación: {location}\n')

def scrap_linkedin():
    url = 'https://www.linkedin.com/jobs/search/?keywords=desarrollador%20web&location=A%20Coru%C3%B1a&geoId=100471030&trk=public_jobs_jobs-search-bar_search-submit&remote=TRUE'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    job_elements = soup.find_all('li', class_='result-card')

    for job_element in job_elements:
        title = job_element.find('h3', class_='').text.strip()
        company = job_element.find('h4', class_='').text.strip()
        location = job_element.find('span', class_='').text.strip()
        print(f'Título: {title}\nEmpresa: {company}\nUbicación: {location}\n')

def scrap_tecnoempleo():
    url = 'https://www.tecnoempleo.com/ofertas-trabajo/?te=desarrollador+full+stack&pr=#buscador-ofertas'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    job_elements = soup.find_all('div', class_='ofertas-listado')
    
    for job_element in job_elements:
        title = job_element.find('h3').text.strip()
        company = job_element.find('a', class_='text_primary').text.strip()
        location = job_element.find('span', class_='hidden-md-down text-grey-800').text.strip()
        print(f'Título: {title}\nEmpresa: {company}\nUbicación: {location}\n')

if __name__ == '__main__':
    print('ofertas de trabajo en Infojobs:')
    scrap_infojobs()
    print('ofertas de trabajo en LinkedIn:')
    scrap_linkedin()
    print('ofertas de trabajo en Tecnoempleo:')
    scrap_tecnoempleo()
