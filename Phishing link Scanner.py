import tldextract
import Levenshtein  as lv

legit_links = ['google.com', 'facebook.com', 'youtube.com', 'amazon.com', 'wikipedia.org', 'twitter.com', 'instagram.com', 'linkedin.com', 'reddit.com', 'pinterest.com', 'netflix.com', 'ebay.com', 'microsoft.com', 'apple.com', 'adobe.com', 'wordpress.com', 'tumblr.com', 'flickr.com', 'dropbox.com', 'paypal.com', 'spotify.com', 'quora.com', 'stackoverflow.com', 'github.com', 'medium.com', 'nytimes.com', 'bbc.com', 'cnn.com', 'forbes.com', 'bloomberg.com', 'huffpost.com', 'theguardian.com', 'washingtonpost.com' 'nbcnews.com', 'abcnews.go.com']


scan_links = ['you.be']

def extract_domain_parts(url):
    extracted = tldextract.extract(url)
    return extracted.subdomain, extracted.domain, extracted.suffix

def possibly_misspelled(domain, legit_links, threshold=1.0):
    for legit_domain in legit_links:
        similarity = lv.ratio(domain, legit_domain)
        if similarity >= threshold:
            return False # Its a legitimate domain
    return True # No close match found, possibly misspelled

def is_phishing_url(url, legit_links):
    subdomain, domain, suffix = extract_domain_parts(url)

    # Check if its a known legitimate domain
    if f"{domain}.{suffix}" in legit_links:
        return False
    
    # Check for misspelled domain  names
    if possibly_misspelled(domain, legit_links):
        print(f"Potential phishing detected: {url}")
        return True
    
    # You can add more checks  here, like suspicious subdomains

    return False

# comment
if __name__ == '__main__':
    for url in scan_links:
        is_phishing_url(url, legit_links)
