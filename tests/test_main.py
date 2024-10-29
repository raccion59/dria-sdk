import json
import os
import asyncio
from dria.factory import (
    Simple,
    StructRAGAlgorithm,
    StructRAGGraph,
    StructRAGCatalogue,
    StructRAGTable,
    StructRAGSynthesize,
    StructRAGSimulate,
    StructRAGJudge,
    StructRAGAnswer,
    StructRAGDecompose,
    StructRAGExtract,
    SubTopicPipeline,
)
from dria.client import Dria
from dria.models import Task, Model

from dria.factory import SubTopicPipeline
from dria.pipelines import PipelineConfig
from dria.client import Dria
from dria.factory import Simple
from dria.models import Model
from dria.batches import ParallelSingletonExecutor
import asyncio
from itertools import chain
from typing import List, Optional

dria = Dria(rpc_token=os.environ["DRIA_RPC_TOKEN"])


async def batch(instructions, singleton_instance, models: List[Model]):
    dria_client = Dria()
    singleton = singleton_instance()
    executor = ParallelSingletonExecutor(dria_client, singleton, batch_size=2000)
    executor.set_models(models)
    executor.load_instructions(instructions)
    return await executor.run()


def batch_run(instructions, instance, models: Optional[List[Model]] = None):
    print(instance.__name__)
    print("Number of instructions: ", len(instructions))

    if not models:
        models = [Model.GEMINI_15_PRO, Model.QWEN2_5_32B_FP16, Model.GPT4O]

    results = asyncio.run(batch(instructions, instance, models))
    with open(f"results_{instance.__name__}.json", "w") as f:
        f.write(json.dumps(results, indent=2))


if __name__ == "__main__":

    synthesize = False
    simulate = False
    judge = True

    if synthesize:

        seeds = [
            "Ancient Civilizations",
            "Medieval History",
            "Modern History",
            "World History",
            "American History",
            "European History",
            "Asian History",
            "African History",
            "Historiography",
            "Historical Methods",
            "Historical Sources",
            "Historical Interpretation",
            "Social History",
            "Political History",
            "Economic History",
            "Cultural History",
            "Military History",
            "Science and Technology History",
            "History of Art",
            "History of Literature",
            "History of Music",
            "History of Religion",
            "History of Philosophy",
            "History of Education",
            "History of Medicine",
            "History of Law",
            "History of Gender",
            "History of Race",
            "History of Immigration",
            "History of Globalization",
            "History of the Environment",
            "History of Climate Change",
            "History of the Internet",
            "History of Artificial Intelligence",
            "History of the Future",
            "Literary Genres and Forms",
            "Historical Periods and Movements",
            "Literary Theory and Criticism",
            "Authorship and Writing Process",
            "Character Development and Plot",
            "Themes and Motifs in Literature",
            "Symbolism and Imagery",
            "Language and Style",
            "Reading and Interpretation",
            "Literary History and Influences",
            "Social and Cultural Context",
            "Literary Canon and Diversity",
            "Adaptation and Transformation",
            "Literature and Society",
            "Literature and Psychology",
            "Literature and Philosophy",
            "Metaphysics",
            "Epistemology",
            "Ethics",
            "Logic",
            "Political Philosophy",
            "Philosophy of Mind",
            "Philosophy of Science",
            "Philosophy of Language",
            "History of Philosophy",
            "Contemporary Philosophy",
            "Eastern Philosophy",
            "Western Philosophy",
            "Existentialism",
            "Nihilism",
            "Postmodernism",
            "Feminist Philosophy",
            "Environmental Philosophy",
            "Biological Psychology",
            "Cognitive Processes",
            "Developmental Stages",
            "Social Influences",
            "Personality Theories",
            "Mental Health Disorders",
            "Psychological Assessment",
            "Therapeutic Approaches",
            "Research Methods",
            "Cellular Biology",
            "Genetics and Heredity",
            "Evolution and Biodiversity",
            "Ecology and Ecosystems",
            "Human Biology and Health",
            "Biotechnology and Genetic Engineering",
            "Molecular Biology and Biochemistry",
            "Anatomy and Physiology",
            "Microbiology and Immunology",
            "Plant Biology and Botany",
            "Zoology and Animal Behavior",
            "Bioethics and Society",
            "Atomic Structure and Bonding",
            "Chemical Reactions and Stoichiometry",
            "States of Matter",
            "Solutions and Mixtures",
            "Thermochemistry",
            "Equilibrium and Kinetics",
            "Acids and Bases",
            "Redox Reactions",
            "Organic Chemistry",
            "Analytical Chemistry",
            "Biochemistry",
            "Environmental Chemistry",
            "Materials Chemistry",
            "Nuclear Chemistry",
            "Computational Chemistry",
            "History of Chemistry",
            "Famous Chemists and Discoveries",
            "Chemistry in Everyday Life",
            "Chemistry and Society",
            "Careers in Chemistry",
            "Celestial Objects and Phenomena",
            "Solar System and Beyond",
            "Stars and Stellar Evolution",
            "Galaxies and Cosmology",
            "Astrophysics and Fundamental Forces",
            "Observational Astronomy and Telescopes",
            "Space Exploration and Missions",
            "History of Astronomy",
            "Astrobiology and the Search for Life",
            "Astrophysics and Fundamental Forces",
            "Astronomy and Culture",
            "Engineering Disciplines",
            "Engineering Design Process",
            "Engineering Ethics and Responsibility",
            "Engineering Materials and Manufacturing",
            "Engineering Mechanics and Statics",
            "Engineering Thermodynamics and Heat Transfer",
            "Engineering Fluid Mechanics",
            "Engineering Project Management",
            "Engineering and Sustainability",
            "Engineering in Society and Culture",
            "Engineering Education and Training",
            "Emerging Technologies in Engineering",
            "Engineering for Global Development",
            "Microeconomics",
            "Macroeconomics",
            "Economic Systems",
            "Market Structures",
            "Supply and Demand",
            "Economic Growth",
            "Inflation and Deflation",
            "International Trade",
            "Labor Economics",
            "Financial Markets",
            "Government Economic Policy",
            "Behavioral Economics",
            "Economic History",
            "Economic Development",
            "Environmental Economics",
            "Economic Inequality",
            "Physical Geography",
            "Human Geography",
            "Geographic Information Systems (GIS)",
            "Cartography and Mapping",
            "Climate and Weather",
            "Landforms and Geology",
            "Population Distribution and Density",
            "Urban Geography",
            "Environmental Geography",
            "Economic Geography",
            "Political Geography",
            "Cultural Geography",
            "Remote Sensing and Aerial Photography",
            "Geographic Data Analysis",
            "Geography in Education",
            "Geography and Sustainability",
            "Geographic Research Methods",
            "History of Geographic Thought",
            "History of political systems",
            "Major political ideologies",
            "Global political alliances",
            "Elections and voting processes",
            "Political economy analysis",
            "International relations theory",
            "Policy making and implementation",
            "Camera fundamentals and types",
            "Composition and framing techniques",
            "Lighting and exposure control",
            "Post-processing and editing",
            "Photography genres and styles",
            "History of photography",
            "Photography equipment and technology",
            "Business of photography",
            "Photography ethics and copyright",
            "Photography for social impact",
            "Digital photography and its impact",
            "Photography as an art form",
            "The future of photography",
            "Business Strategy and Planning",
            "Marketing and Sales",
            "Finance and Accounting",
            "Operations Management",
            "Human Resources Management",
            "Entrepreneurship and Innovation",
            "Organizational Behavior",
            "Business Ethics and Social Responsibility",
            "International Business",
            "E-commerce and Digital Business",
            "Business Analytics and Data Science",
            "Business Law and Regulation",
            "History of Sports",
            "Types of Sports",
            "Sports Equipment and Technology",
            "Sports Training and Conditioning",
            "Sports Nutrition",
            "Sports Injuries and Rehabilitation",
            "Sports Psychology",
            "Sports Officiating",
            "Sports Broadcasting and Media",
            "Sports Marketing and Sponsorship",
            "Professional Sports Leagues",
            "Amateur Sports and Recreation",
            "Sports and Society",
            "Sports and Culture",
            "Gender and Sports",
            "Race and Sports",
            "Sports and Politics",
            "Sports and Globalization",
            "Sports Ethics and Fair Play",
            "Sports and the Environment",
            "Future of Sports",
            "History of cinema",
            "Film genres and styles",
            "Directing techniques and approaches",
            "Screenwriting and script analysis",
            "Cinematography and visual storytelling",
            "Editing and post-production processes",
            "Film sound and music scoring",
            "Acting methods and performance styles",
            "Independent vs. studio filmmaking",
            "International film industries",
            "Film criticism and analysis",
            "Impact of digital technology in film",
            "Representation and diversity in cinema",
            "Film festivals and markets",
            "Future trends in filmmaking",
            "Microeconomics",
            "Macroeconomics",
            "Economic Systems",
            "Economic Growth and Development",
            "International Economics",
            "Labor Economics",
            "Financial Economics",
            "Behavioral Economics",
            "Economic History",
            "Economic Policy",
            "Religious History and Origins",
            "Major World Religions",
            "Religious Beliefs and Practices",
            "Religious Texts and Scriptures",
            "Religious Rituals and Ceremonies",
            "Religious Ethics and Morality",
            "Religious Institutions and Organizations",
            "Religious Art and Architecture",
            "Religious Music and Literature",
            "Religious Festivals and Holidays",
            "Religious Experiences and Mysticism",
            "Religious Social Movements",
            "Religious Conflict and Violence",
            "Religious Tolerance and Pluralism",
            "Religious Freedom and Rights",
            "Religion and Science",
            "Religion and Politics",
            "Religion and Gender",
            "Religion and Culture",
            "Religion and Psychology",
            "Religion and Sociology",
            "Religion in the Modern World",
            "Human Origins and Evolution",
            "Cultural Anthropology",
            "Archaeology and Material Culture",
            "Linguistic Anthropology",
            "Biological Anthropology",
            "Social and Cultural Change",
            "Ethnographic Methods",
            "Anthropology of Religion",
            "Medical Anthropology",
            "Applied Anthropology",
            "Global Anthropology",
            "Anthropology of the Body",
            "Gender and Sexuality",
            "Race and Ethnicity",
            "Environmental Anthropology",
            "History of theater",
            "Types of theater performances",
            "Influential playwrights and directors",
            "Set design and stage technology",
            "Theater production process",
            "Role of theater in society",
            "Theater acting techniques",
            "Musical theater versus dramatic theater",
            "Understanding theater criticism",
            "The impact of digital technology on theater",
            "Regional and cultural variations in theater",
            "Role of costume and makeup in theater",
            "Theater education and training",
            "Prominent theater festivals worldwide",
            "Audience engagement in theater",
            "Phonetics & Phonology",
            "Morphology & Word Formation",
            "Syntax & Sentence Structure",
            "Semantics & Meaning",
            "Pragmatics & Language Use",
            "Sociolinguistics",
            "Psycholinguistics",
            "Neurolinguistics",
            "Computational Linguistics",
            "Historical Linguistics",
            "Language Acquisition",
            "Language Change",
            "Language Documentation",
            "Language & Culture",
            "Language & Cognition",
            "Historical development of law",
            "Theories of justice and morality",
            "Key legal concepts and terminology",
            "International law and global governance",
            "Domestic law and national jurisdiction",
            "Comparative law and legal systems",
            "Criminal law and punishment theory",
            "Contract law and business regulations",
            "Tort law and personal liability",
            "Labor law and employment rights",
            "Family law and relationships",
            "Environmental law and sustainability",
            "Intellectual property law and innovation",
            "Constitutional law and government power",
            "Number Theory",
            "Algebra",
            "Geometry",
            "Calculus",
            "Statistics",
            "Probability",
            "Discrete Mathematics",
            "Applied Mathematics",
            "Mathematical Logic",
            "Set Theory",
            "Topology",
            "Differential Equations",
            "Numerical Analysis",
            "Music History and Evolution",
            "Music Theory and Composition",
            "Musical Instruments and Technology",
            "Genres and Styles of Music",
            "Music Production and Recording",
            "Music Performance and Interpretation",
            "Music and Culture",
            "Music and Emotion",
            "Music and Cognition",
            "Music Therapy and Healing",
            "Music Industry and Business",
            "Music Education and Pedagogy",
            "Physical Geography",
            "Human Geography",
            "Geographic Information Systems (GIS)",
            "Cartography and Mapmaking",
            "Climate and Weather Patterns",
            "Landforms and Topography",
            "Population Distribution and Density",
            "Environmental Geography",
            "Urban Geography",
            "Regional Geography",
            "Geopolitics and International Relations",
            "History of Geography",
            "Geographic Data Analysis",
            "Remote Sensing and Aerial Photography",
            "Geographic Education and Outreach",
            "Types of dance styles",
            "Dance techniques and training methods",
            "Cultural significance of dance",
            "Psychological benefits of dance",
            "Technological advancements in dance education",
            "Dance as a form of expression",
            "History of technology",
            "Theoretical foundations",
            "Recent technological advancements",
            "Technology in business",
            "Ethical implications of technology",
            "Futuristic technologies",
            "History of Computing",
            "Computer Architecture",
            "Operating Systems",
            "Programming Languages",
            "Software Development",
            "Computer Networks",
            "Data Structures and Algorithms",
            "Artificial Intelligence",
            "Cybersecurity",
            "Computer Graphics",
            "Computer Science Education",
            "Impact of Computers on Society",
            "Culinary Techniques and Skills",
            "Global Cuisine and Regional Specialties",
            "Food Science and Nutrition",
            "Culinary History and Traditions",
            "Restaurant Management and Operations",
            "Food Safety and Sanitation",
            "Culinary Arts Education and Training",
            "Food Styling and Presentation",
            "Culinary Trends and Innovation",
            "The Art of Flavor and Taste",
            "Food and Culture",
            "Sustainable Food Practices",
            "Effective verbal communication skills",
            "Nonverbal cues and body language",
            "Interpersonal conflict resolution techniques",
            "Public speaking and presentation strategies",
            "Cross-cultural communication challenges",
            "Digital communication tools and platforms",
            "Newtonian Mechanics",
            "Lagrangian and Hamiltonian Mechanics",
            "Kinematics and Dynamics",
            "Rotational Motion and Angular Momentum",
            "Gravitation and Celestial Mechanics",
            "Fluid Mechanics",
            "Waves and Oscillations",
            "Elasticity and Deformation",
            "Thermodynamics and Statistical Mechanics",
            "Modern Art Movements",
            "Key Modern Artists",
            "Modern Art Techniques",
            "Modern Art and Society",
            "Modern Art and Technology",
            "Modern Art Criticism",
            "Modern Art Collections",
            "Modern Art in Popular Culture",
            "Art History and Movements",
            "Artistic Techniques and Styles",
            "Art Appreciation and Criticism",
            "Art as a Form of Communication",
            "Art and Society",
            "Art and Culture",
            "Art and Technology",
            "Art and the Environment",
            "Art Education and Training",
            "Art Market and Economics",
            "Wildlife Conservation Efforts",
            "Biodiversity and Ecosystem Roles",
            "Human-Wildlife Interactions",
            "Wildlife Management Practices",
            "Endangered and Threatened Species",
            "Wildlife Habitat Loss and Fragmentation",
            "Wildlife Disease and Health",
            "Wildlife Tourism and Recreation",
            "Wildlife Trade and Trafficking",
            "Climate Change Impacts on Wildlife",
            "History of Sports",
            "Types of Sports",
            "Sports and Culture",
            "Sports and Technology",
            "Sports and Health",
            "Sports and Business",
            "Sports and Politics",
            "Sports and Social Justice",
            "Sports and Gender",
            "Sports and Disability",
            "Sports and Media",
            "Sports and Entertainment",
            "Sports and Education",
            "Sports and Psychology",
            "Sports and Nutrition",
            "Sports and Training",
            "Sports and Performance",
            "Sports and Injury",
            "Sports and Safety",
            "Sports and Ethics",
            "Sports and Law",
            "Sports and Economics",
            "Sports and Globalization",
            "Sports and Sustainability",
            "Future of Sports",
            "History of medical practices",
            "Epidemiology basics and importance",
            "Molecular biology in drug development",
            "Surgical techniques evolution",
            "Global healthcare systems comparison",
            "Medical ethics and patient rights",
            "Infectious diseases control strategies",
            "Chronic disease management approaches",
            "Mental health awareness and treatment",
            "Biomaterials for implants and prosthetics",
            "Regenerative medicine applications",
            "Nanomedicine and targeted therapies",
            "Healthcare policy and reform trends",
            "Pharmaceutical industry operations",
            "Evidence-based medicine practices",
            "Public health interventions effectiveness",
            "Social Structure and Inequality",
            "Culture and Society",
            "Socialization and Identity",
            "Social Institutions and Organizations",
            "Social Change and Movements",
            "Methods of Sociological Research",
            "Sociology of Everyday Life",
            "Sociology of Work and Economy",
            "Sociology of Health and Illness",
            "Sociology of Gender and Sexuality",
            "Sociology of Race and Ethnicity",
            "Sociology of Religion",
            "Sociology of Education",
            "Sociology of the Family",
            "Sociology of the Environment",
            "Sociology of Technology",
            "Global Sociology",
            "Applied Sociology",
            "Microeconomics",
            "Macroeconomics",
            "Economic Systems",
            "Economic Growth and Development",
            "International Trade",
            "Labor Economics",
            "Financial Markets",
            "Government Policy",
            "Economic History",
            "Behavioral Economics",
            "Econometrics",
            "Economic Inequality",
            "Environmental Economics",
            "Economic Modeling",
            "Historical background of education",
            "Key theories and concepts in education",
            "Current research and developments in education",
            "Practical applications of education in industry",
            "Ethical considerations in education policy",
            "Future trends and predictions in education",
            "History of Computing",
            "Computer Architecture",
            "Operating Systems",
            "Programming Languages",
            "Software Development",
            "Computer Networks",
            "Data Storage and Retrieval",
            "Computer Security",
            "Artificial Intelligence",
            "Computer Graphics",
            "Human-Computer Interaction",
            "Computer Ethics",
            "Social Impact of Computers",
            "Future of Computing",
        ]
        # seeds = ['History', 'Psychology', 'Economics', 'Political Science', 'Linguistics', 'Astronomy', 'Chemistry', 'Biology', 'Environmental Science', 'Culinary Arts', 'Architecture', 'Wildlife', 'Computers', 'Food', 'Physics', 'Communication', 'Music', 'Sociology', 'Art', 'Modern Art', 'Mechanical Physics', 'Mathematics', 'Philosophy', 'Geography', 'Anthropology', 'Literature', 'Theater', 'Film', 'Education', 'Business', 'Engineering', 'Medicine', 'Law', 'Public Health', 'Data Science', 'Artificial Intelligence', 'Robotics', 'Genetics', 'Neuroscience', 'Astrophysics', 'Oceanography', 'Meteorology', 'Geology', 'Agronomy', 'Zoology', 'Botany', 'History', 'Psychology', 'Economics', 'Political Science', 'Linguistics', 'Astronomy', 'Chemistry', 'Biology', 'Environmental Science', 'Culinary Arts', 'Architecture', 'Wildlife', 'Computers', 'Food', 'Physics', 'Communication', 'Music', 'Sociology', 'Art', 'Modern Art', 'Mechanical Physics']
        batch_run(
            [{"seed": seed} for seed in seeds],
            StructRAGSynthesize,
            [
                Model.GEMINI_15_PRO,
                Model.GEMINI_15_FLASH,
                Model.GPT4O,
                Model.QWEN2_5_32B_FP16,
                Model.LLAMA3_1_8B_FP16,
                Model.LLAMA3_1_8B_FP16,
            ],
        )

    if simulate:
        with open(f"results_{StructRAGSynthesize.__name__}.json", "r") as f:
            data = json.load(f)
        datax = list(chain(*data))

        batch_run(
            [
                {"query": d["query"], "documents_info": d["documents_info"]}
                for d in datax
            ],
            StructRAGSimulate,
            [
                Model.GEMINI_15_PRO,
                Model.GEMINI_15_FLASH,
                Model.GPT4O,
                Model.QWEN2_5_32B_FP16,
                Model.LLAMA3_1_8B_FP16,
                Model.QWEN2_5_32B_FP16,
            ],
        )

    if judge:
        with open(f"results_{StructRAGSimulate.__name__}.json", "r") as f:
            data = json.load(f)

        batch_run(
            [
                {
                    "query": d["query"],
                    "documents_info": d["documents_info"],
                    "solutions": d["solutions"],
                }
                for d in data
            ],
            StructRAGJudge,
        )

    with open(f"results_{StructRAGJudge.__name__}.json", "r") as f:
        data = json.load(f)
    datax = list(chain(*data))
