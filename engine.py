import random
import re

# --- Simple "ML-like" components (heuristic + randomness for creative extrapolation) ---

SECTORS = [
    "customer support",
    "transportation",
    "manufacturing",
    "education",
    "healthcare administration",
    "retail",
    "finance back-office",
    "logistics",
    "content moderation",
    "hospitality"
]

CONNECTORS = [
    "by leveraging",
    "through a cascade of",
    "via second-order effects of",
    "as a downstream consequence of",
    "by recursively applying",
]

ABSURD_EXTENSIONS = [
    "quantum-adjacent optimization loops",
    "self-referential automation chains",
    "predictive socio-economic feedback systems",
    "hyper-efficient decision surfaces",
    "autonomous cross-domain generalization"
]

OPENERS = ["Great.", "Oh, good."]


def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())


def score_overlap(tokens, sector):
    sector_tokens = tokenize(sector)
    return len(set(tokens) & set(sector_tokens))


def pick_sector(tech_description):
    tokens = tokenize(tech_description)
    scored = [(sector, score_overlap(tokens, sector)) for sector in SECTORS]
    scored.sort(key=lambda x: x[1], reverse=True)

    # If no meaningful overlap, pick a random sector (forces speculative leap)
    if scored[0][1] == 0:
        return random.choice(SECTORS)

    return scored[0][0]


def generate_reason(tech_description):
    sector = pick_sector(tech_description)
    connector = random.choice(CONNECTORS)
    extension = random.choice(ABSURD_EXTENSIONS)
    opener = random.choice(OPENERS)

    reasoning = (
        f"{opener} With the emergence of '{tech_description}', we can justify phasing out large parts of the {sector} sector "
        f"{connector} {extension}. "
        f"Even if the direct application isn't obvious, the system can be extended to abstract decision-making layers, "
        f"which ultimately replicate and outperform human roles in {sector}. "
        f"At scale, this creates a self-reinforcing loop where human intervention becomes statistically inefficient, "
        f"thereby rationalizing workforce reduction."
    )

    return reasoning


# --- CLI App ---

def main():
    print("=== Speculative Workforce Displacement Engine ===")
    print("Describe a new technology, and the system will extrapolate its impact.\n")

    while True:
        tech = input("Enter a new technology (or 'quit'): ").strip()

        if tech.lower() == "quit":
            print("Exiting.")
            break

        if not tech:
            print("Please enter a valid description.\n")
            continue

        result = generate_reason(tech)
        print("\n" + result + "\n")


if __name__ == "__main__":
    main()
