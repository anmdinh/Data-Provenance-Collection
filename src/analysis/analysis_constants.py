
TOS_AI_SCRAPING_VERDICT_MAPPER = {
    1: "Prohibits Scraping & AI",
    2: "Prohibits Scraping",
    3: "Prohibits AI",
    4: "Conditional Restrictions",
    5: "No Restrictions",
}

CONTENT_DOMAIN_CATEGORY_COMPRESSION = {
    "News": ["News/Periodicals"],
    "General Information & Education": ['Education/Knowledge', "General"],
    "Science, Academia, & Technology": ['Academic', 'Biomedical/Health', 'Technology/Code', ],
    "Social Media/Forums": ["Social Media/Forums"],
    "Business & E-Commerce": ["E-Commerce", "Business/Finance/Organizational"],
    "Entertainment & Culture": ['Cultural/Artistic', 'Social/Lifestyle', 'Entertainment', 'Reviews', 'Travel', 'Religion'],
    "Books": ["Books"],
    "Legal & Policy": ['Government/Policy', 'Legal'],
    "Blogs": ['Blogs'],
    "Other": ["Other"],
}
INVERSE_CONTENT_DOMAIN_CATEGORY_COMPRESSION = {
    v: k for k, vs in CONTENT_DOMAIN_CATEGORY_COMPRESSION.items() for v in vs
}


CONTENT_DOMAIN_MAPPING = {
    'News/Periodicals': ['News', 'Current affairs, sports', 'News archives', 'Newsletter', 'Articles', 'obituary'],
    'Education/Knowledge': ['Education/Knowledge', 'info about schools', 'Education/Knowledge', 'Exams', 'Company website and services'],
    'Entertainment': [
        'Entertainment', 'Anime', 'Sports', 'Gaming', 'Sport', 'Sports/games', 'University sports', 'Game website', 'Adult stories website',
        'Porn website', 'Escort procurement', 'online classes', 'astrology website'
    ],
    'Business/Finance/Organizational': [
        'Business/Finance', 'Finance', 'Business directory', 'B2B marketplace', 'Business finder',
        'Personal business', 'Management Consultant', 'Company portal', 'Company website',
        'Fundraising portal', 'Marketing', 'Non-profit agency', 'Non Profit', 'Non-profit/Charity',
        'Nonprofit organization ', 'Non-Profit', 'Non Profit, Recycling', 'Freelancer designer', 
        'Freelancer designer & developer', 'Application website', 'Organizations', 'Charity', 'Donation', 
        'Fundraising/Donation', 'Organization description', 'Insurance company website',
        'Security', 'jobs', 'real estate', 'hotel', 'charity , non-profit', 'beauty', 'recruiters',
        'environmental org.', 'visually impaired people support organization', 'violence control support org.', 'organization for fresh water solutions',
        'charity organization', 'charity org.'  
    ],
    'Technology/Code': [
        'Technology/Code', 'Search engine', 'Search engine portal', 'Internet RFC/STD/FYI/BCP document archives', 'Search tool',
        'Web ring', 'Mailing list', 'directory / webring', 'artificial intelligence'
    ],
    'E-Commerce': ['E-Commerce', 'Ecommerce', 'E-shop page', 'Online shop', 'Services', 'vehicle and parts buy and sell'],
    'Academic': ['Academic', 'Social sciences', 'Science', 'Ideologies and thought', 'Religion and Philosophy', 'ancestry analysis'],
    'General': [
        'General', 'Prototype', 'Forum', 'Encyclopedia', 'survey portal'
    ],
    'Cultural/Artistic': [
        'Cultural/Artistic', 'Painting', 'reddit posts', 'Music', 'creativity'
    ],
    'Social/Lifestyle': [
        'Social/Lifestyle', 'Social', 'Lifestyle', 'Home improvement / design', 'Fitness',
        'Home improvement', 'Human Rights / NGO', 'Women Empowerment', 'geographic and demographic analytics',
        'Food', 'Recipes', 'Beverage', 'Menu', 'nature', 'dogs', 'photography', 'hoboken garden club',
        'city club', 'nature, camping'
    ],
    'Reviews': ['Reviews', 'Review portal', 'Images database', 'digital archive'],
    'Government/Policy': ['Government/Policy', 'Politics', 'Military', 'Employment', 'Service', 'firestation', 'ex-police association'],
    'Biomedical/Health': ['Biomedical/Health', 'Biology', 'Medical', 'Health'],
    'Books': ['Books', 'Documents', 'article , blog', 'music , blog'],
    'Legal': ['Legal'],
    'Religion': ['Religion', 'Religion/Christianity', 'Religious website'],
    'Travel': ['Travel', 'Travel and tourism', 'Travel information', 'Trips'],
    'Blogs': ['Blog', 'Blogs', 'personal blog', 'personal bio', 'Personal website', 'personal website', 'Personal page', 'personal webpage', 'personal portfolio site'],
}
CONTENT_DOMAIN_INVERSE_MAPPING = {v.lower().strip(): k for k, vs in CONTENT_DOMAIN_MAPPING.items() for v in vs}


WEBSITE_SERVICE_MAPPING = {
   'News/Periodicals': [
        'Australian news and financial site providing video, audio, and stories',
        'Broadcasting and radio shows while communicating with listeners',
        'Contains a wide variety of different books, audio, and articles',
        'Daily tips',
        'Electronic publishing sit containing a variety of content',
        'Jamaica news, lifestyle, and entertainment articles',
        'Journal',
        'Lifestyle magazine',
        'News and articles for comic books',
        'News and broadcasting site providing video, audio, and stories',
        'News and entertainment site for pop culture',
        'News and lifestyle site for Kitsap providing video, audio, and stories',
        'News and lifestyle site providing video, audio, and stories',
        'News and technology site',
        'News articles about different social trends',
        'News articles and reviews for biking',
        'News site providing video and stories',
        'News site providing video, audio, and stories',
        'Periodicals',
        'Radio Station',
        'A news and lifestyle website for Cape Cod and state of Massachusetts',
        'Argentinian racing content',
        'Books,ebooks,magazine',
        'Contains articles about current events in Sarasota',
        'Contains articles about current events in Utah',
        'Current events in Utah and news articles',
        'Energy price news',
        'India news articles and videos',
        'Indian consumer technology news',
        'Lifestyle articles portal',
        'Local news articles for Colorado',
        'Middle East news articles',
        'Mix of news and fan content',
        'News and Search Services',
        'News and insights',
        'News and reviews portal',
        'News articles for Ghana',
        'News articles, podcasts, and radio about current events',
        'News collection',
        'News for tabletop and rpg games and community forums',
        'News site',
        'News site for different medical and life sciences articles',
        'News website and blog',
        'News, weather, and general info',
        'Opinion pieces on news stories',
        'Periodical',
        'Podcasts',
        'Regional sports news',
        'TV Station',
        'Technology newsletter and articles',
        'Telegraph India news articles',
        'Video game news',
        'Video game reviews',
        'entertainment tv channel',
        'non-official news media',
        'non-periodical news',
        'religious magazine',
        'satire'
    ],
    'Organization/Personal Website': [
        'A member and association organization for bartenders',
        'A website where users can upload and download books and other publications',
        'Artist website',
        'Astrology website',
        'Business / Finance',
        'Business directory',
        'Camera and Security Systems',
        'Charity',
        'CharityAutism',
        'Chiropractic, Nutrition, therapies services',
        'Company locations for firestone automotive parts and services',
        'Company website',
        'Dental Health',
        'Employee Training',
        'Finance advise & services',
        'Financial Planning',
        'Financial information',
        'Find and hire freelancers',
        'Find companies for different home services, cleaning, and other needs.',
        'Information about the services offered by the manufacturing company',
        'Insurance Services',
        'Internation Organization website',
        'Local sport league organization website',
        'NGO',
        'Non Profit',
        'Non-profit',
        'Nonprofit Website',
        'Nonprofit website',
        'Organization',
        'Organization website',
        'Packaging and supplies services',
        'Personal Blog',
        'Personal Injury LawGraphics and web designing',
        'Personal Website',
        'Personal website',
        'Property Selling',
        'Religious organization website',
        'Restaurant',
        'Road Running',
        'Social/Human rights',
        'Sports website for a university',
        'Tech storage solutions',
        'investment management',
        'nonprofit organization',
        'personal site',
        'personal webpage',
        'personal website',
        'school website',
        'web ring',
        'information website',
        'accommodation',
        'insurance services',
        'corporate security and intelligence',
        'security assessments to managed services and disaster recovery',
        'planting, land protection',
        'horse riding',
        'traveling',
        'packaging services',
        'marketing',
        'health',
        'designing',
        'hearing care',
        'architecture',
        'medical devices',
        'food, restaurant',
        'beauty therapy',
        'art',
        'trips',
        'cleaning',
        'storage',
        'sustainable products',
        'construction',
        'sport',
        'heart valves, AI',
        'medical transport',
        'sports',
        'library',
        'safety',
        'petrol station',
        'articles',
        'dictionary',
        'graphite',
        'photography, company website',
        'research group',
        'graphic design, company website',
        'cafe',
        'hotel, company website',
        'dental clinic',
        'vehicle and parts buy and sell',
        'network',
        'platform for discussions, insights',
        'defense and security solutions, company website',
        'manufacturing, installation, company website',
        'waste solutions, company website',
        'architecture, company website',
        'blood test, treatment',
        'steel supply and services, company website',
        'windows & doors UPVC repairs, locks & hinges, company website',
        'online platform',
        'lab',
        'venue, company website',
        'platform to find professionals',
        'club',
        'association',
        'camp ground',
        'agency',
        'article, blog',
        'digital media',
        'restaurant and bar',
        'ornithologists group',
        'religious community',
        'public program',
        'non-profit organization',
        'marketing, SEO',
        'festival',
        'karate, company website',
        'rental, company website',
        'religious',
        'dog\'s competitions',
        'Brazilian art form',
        'online booking, company website',
        'company website, apps',
        'marketing automation, website maintenance, content management, company website',
        'company website, roofing',
        'company website, courses',
        'animals',
        'graphic design, SEO, website design',
        'online service',
        'vote',
        'legal',
        'technology',
        'software',
        'entertainment',
        'search services',
        'museum',
        'novels',
        'online media',
        'skills',
        'mailing list',
        'religion',
        'menu',
        'recipes',
        'culture/politics',
        'editor reviews',
        'music',
        'furnishment',
        'culture',
        'petition',
        'editor reviews/tips',
        'chum',
        'financial reports and analysis',
        'services'
    ],
    'Encyclopedia/Database': [
        '& Encyclopedia',
        'Article directory',
        'Collection of photography guides',
        'Compilation of books, historic and other academic works at Tufts',
        'Compilation of different medical research papers',
        'Compilation of different podcasts',
        'Compilation of different sermons',
        'Compilation of tumblr blogs',
        'Contains a repository of different fantasy novels and books',
        'Database of sermons',
        'Education/Knowledge',
        'Encyclopedia',
        'Encyclopedia/Database',
        'Information',
        'Internet RFC/STD/FYI/BCP document archives',
        'Law resources',
        'Legal Research Database',
        'Legal database',
        'Mail archive',
        'Oncology research papers and archives',
        'Portal',
        'Religion-based library',
        'Search',
        'Search engine',
        'Search for books',
        'Search tool',
        'Tracking GIT changes for GNU OS',
        'User can access coupon codes for different services',
        'Wiki site for creative writing',
        'Wiki site for fan translation',
        'Wikipedia skin for easier reading',
        'jobs database',
        'online library',
        'patents website',
        'tool for web traffic overview',
        'blood test, treatment',
        'dictionary',
        'graphite'
    ],
    'E-Commerce': [
        'A website for a software company providing coding and other services',
        'Book self-publishing website',
        'Bookings website for sailing trips',
        'Business Apps',
        'Buy and sell different books online',
        'Computer repairing',
        'Coupon codes',
        'Designing and editing',
        'E-Commerce',
        'saas',
        'buy and sell',
        'Ecommerce',
        'Find local apartments to rentTravel and Navigation Services',
        'Hair Treatment',
        'Hotel',
        'Paywalled business analysis',
        'Physical store directory',
        'Plant and gardening store',
        'Streaming services',
        'Travel Guide',
        'Travel bookings',
        'Travel guide',
        'Travel website where users can book flights, transportation, hotels, and other accommodations',
        'Wholesale',
        'booking platform',
        'gambling website',
        'independent sellers platform',
        'product website',
        'travel website with curated blogs'
    ],
    'Academic': [
        'A wide variety of technological articles and newsletters',
        'Academic',
        'Academic opportunity search',
        'Clinical and medical podcasts, blogs, news, and videos',
        'Diabetes medical information and articles',
        'Education',
        'Educational resources + review aggregator',
        'Educational study tools',
        'Financial reports, filings, news, and transcripts',
        'Journal,health',
        'Medical and biotech research for immunology',
        'Provides testing for dna, drugs, and other things',
        'USGPO articles and information',
        'academic journal website',
        'education/ courses'
    ],
    'Social Media/Forums': [
        'social media/forum',
        'A forum for obisidian games where users can discuss games and community announcements',
        'A forum for relationship and dating advice with some crafted articles',
        'A forum for users to ask questions about metalworking and model engineering',
        'A forum where users can ask questions about the unity game engine',
        'Advice',
        'Also contains a forum',
        'Also forum/social',
        'An internet archive capture of a gaming article',
        'Blog posts portal',
        'Blogs/forum for building things',
        'Contains user uploaded videos',
        'Crowdfunding platform',
        'Eritrean analysis forum',
        'Fan art website',
        'Find local area businesses',
        'Find user reviews for different products',
        'Forum for different rockstar videogames',
        'Forum for mobile developers and others to ask questions about phones and accessories.',
        'Forum for tech news, computers, and other forms of hardware',
        'Forum for users to discuss body building, fitness, and trt',
        'Forum for users to discuss lucid dreaming experiences',
        'Forums',
        'Forums and community for mothers',
        'Forums for discussing the video game warframe',
        'Game news forum',
        'Gaming community forum where users can comment on gaming videos and have discussions',
        'Gaming website',
        'Health articles for different chronic illnesses and community forums',
        'Information about pregnancy and community forums',
        'Personal blog',
        'Question/Answering portal',
        'Review',
        'Review portal',
        'Review site',
        'Review site / photo aggregator',
        'Reviews',
        'Social Media',
        'Social Media for tech',
        'Social Media/Forums',
        'Social media / forums',
        'Social media book reviews website',
        'Social media/forums',
        'Stack exchange forum for physics questions and answers',
        'Tech product discussion',
        'The 4chan forum',
        'User forums',
        'Users can find local caregivers for different needs',
        'Users rate different movies, tv, and video games',
        'Users talk about different unsolved mysteries and related news',
        'Video game community and forums',
        'Video game, community forum, and wikipedia',
        'and forum',
        'content and forum',
        'forum',
        'forums',
        'law (student) network',
        'old forum no longer available',
        'online community',
        'reddit posts',
        'review platform',
        'social media',
        'platform for discussions, insights',
        'platform to find professionals',
        'articles',
        'article, blog',
        'digital media',
        'blog publishing platform'
    ],
    'Government': [
        'Articles and comments about Australian government and politics',
        'Government',
        'Government records',
        'Government website containing agenda and publications',
        'Governmental information tracking',
        'sustainability website with news and tips'
    ],
    'Blogs': [
        '(single-poster) Blog',
        'Adult stories',
        'Archive of technology blog posts',
        'Blog',
        'Blog directory',
        'Blog platform',
        'Blog system',
        'Blog,Podcast',
        'Blog?',
        'Blogs',
        'Christian opinion website',
        'Climate Blog',
        'Entertaiment blog',
        'Entertainment Blog',
        'Entertainment biographies',
        'Fan fiction for fantasy',
        'Lifestyle',
        'Lifestyle blog',
        'Lifestyle portal',
        'Music and information about a Dutch band',
        'Personal blog',
        'Poetry sharing, reading, and articles',
        'Religious blog style website',
        'Self help site',
        'Technology blog',
        'blog ',
        'blog site for gear review',
        'blog site of a religion group',
        'blog style website for food',
        'blogs',
        'novels website',
        'personal blog'
    ]
}
WEBSITE_SERVICE_INVERSE_MAPPING = {v.lower().strip(): k for k, vs in WEBSITE_SERVICE_MAPPING.items() for v in vs}
