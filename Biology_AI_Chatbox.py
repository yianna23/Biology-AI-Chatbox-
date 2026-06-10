import tkinter as tk
from tkinter import scrolledtext
from difflib import SequenceMatcher
import unicodedata
import re

qa_pairs = [
    (
        "hello hi hey greetings good morning good afternoon good evening",
        "Hello! 🧬 I am your AI Biology Tutor. Ask me anything about biology and I will try to help you with a clear and simple answer!"
    ),
    (
        "what is biology",
        "Biology is the science that studies living organisms, including their structure, function, growth, evolution, and interactions."
    ),
    (
        "what is a cell",
        "A cell is the basic structural and functional unit of life."
    ),
    (
        "difference between plant and animal cell",
        "Plant cells have a cell wall and chloroplasts, while animal cells do not."
    ),
    (
        "what is dna",
        "DNA is the genetic material that contains the instructions for the growth, function, and development of living organisms."
    ),
    (
        "what is rna",
        "RNA helps transfer genetic information and plays an important role in protein synthesis."
    ),
    (
        "what is protein synthesis",
        "Protein synthesis is the process by which cells create proteins using genetic instructions from DNA."
    ),
    (
        "what is photosynthesis",
        "Photosynthesis is the process by which plants use light energy to produce glucose and oxygen from carbon dioxide and water."
    ),
    (
        "photosynthesis equation",
        "6CO₂ + 6H₂O + light → C₆H₁₂O₆ + 6O₂"
    ),
    (
        "what is cellular respiration",
        "Cellular respiration is the process by which cells produce ATP energy from glucose."
    ),
    (
        "difference between mitosis and meiosis",
        "Mitosis produces two identical cells, while meiosis produces four genetically different sex cells."
    ),
    (
        "what is osmosis",
        "Osmosis is the movement of water through a selectively permeable membrane."
    ),
    (
        "what is diffusion",
        "Diffusion is the movement of substances from an area of high concentration to an area of low concentration."
    ),
    (
        "what is homeostasis",
        "Homeostasis is the ability of an organism to maintain stable internal conditions."
    ),
    (
        "what is evolution",
        "Evolution is the process by which living organisms change over time."
    ),
    (
        "who proposed the theory of evolution",
        "Charles Darwin proposed the theory of evolution through natural selection."
    ),
    (
        "what is natural selection",
        "Natural selection is the process in which organisms with helpful adaptations are more likely to survive and reproduce."
    ),
    (
        "what are enzymes",
        "Enzymes are biological catalysts that speed up chemical reactions."
    ),
    (
        "what affects enzyme activity",
        "Temperature, pH, and substrate concentration can affect enzyme activity."
    ),
    (
        "what is genetics",
        "Genetics is the branch of biology that studies heredity and genes."
    ),
    (
        "what is a gene",
        "A gene is a section of DNA that contains instructions for making proteins."
    ),
    (
        "what is a chromosome",
        "Chromosomes are structures made of DNA that carry genetic information."
    ),
    (
        "what is a mutation",
        "A mutation is a change in the DNA sequence."
    ),
    (
        "what does the nucleus do",
        "The nucleus controls the cell's activities and contains DNA."
    ),
    (
        "function of mitochondria",
        "Mitochondria produce ATP energy through cellular respiration."
    ),
    (
        "what are ribosomes",
        "Ribosomes are cell structures involved in protein synthesis."
    ),
    (
        "what is the cell membrane",
        "The cell membrane controls what enters and leaves the cell."
    ),
    (
        "what is ecology",
        "Ecology is the study of interactions between organisms and their environment."
    ),
    (
        "what is an ecosystem",
        "An ecosystem includes living organisms and their environment interacting together."
    ),
    (
        "what is a food chain",
        "A food chain shows how energy is transferred from one organism to another."
    ),
    (
        "what is biodiversity",
        "Biodiversity is the variety of living organisms in an environment."
    ),
    (
        "what is a virus",
        "A virus is a tiny infectious agent that can reproduce only inside living cells."
    ),
    (
        "difference between bacteria and viruses",
        "Bacteria are living single-celled organisms, while viruses need a host cell to reproduce."
    ),
    (
        "what is the immune system",
        "The immune system protects the body from harmful microorganisms and diseases."
    ),
    (
        "what are white blood cells",
        "White blood cells help defend the body against infections."
    ),
    (
        "what is a vaccine",
        "A vaccine trains the immune system to recognize and fight specific pathogens."
    ),
    (
        "what is anatomy",
        "Anatomy is the study of the structure and organs of the body."
    ),
    (
        "what is physiology",
        "Physiology is the study of how organisms and their body systems function."
    ),
    (
        "what are hormones",
        "Hormones are chemical messengers that regulate body functions."
    ),
    (
        "what is reproduction",
        "Reproduction is the process by which organisms produce offspring."
    ),
    (
        "difference between asexual and sexual reproduction",
        "Asexual reproduction involves one parent, while sexual reproduction involves two parents and creates genetic variation."
    ),
    (
        "what is biotechnology",
        "Biotechnology uses biological systems to develop technologies and useful products."
    ),
    (
        "what is crispr",
        "CRISPR is a gene-editing technology that allows scientists to modify DNA."
    ),
    (
        "what is bioinformatics",
        "Bioinformatics combines biology and computer science to analyze biological data."
    ),

    # =====================================================
    # NERVOUS SYSTEM
    # =====================================================
    (
        "what is the nervous system",
        "The nervous system coordinates and controls the body's functions."
    ),
    (
        "what are the parts of the nervous system",
        "The nervous system is divided into the central nervous system and the peripheral nervous system."
    ),
    (
        "what is the central nervous system",
        "The central nervous system consists of the brain and spinal cord."
    ),
    (
        "what is the peripheral nervous system",
        "The peripheral nervous system consists of nerves that connect the body to the central nervous system."
    ),
    (
        "what is the brain",
        "The brain is the organ that controls thoughts, movement, memory, and many body functions."
    ),
    (
        "what is the spinal cord",
        "The spinal cord carries nerve signals between the brain and the rest of the body."
    ),
    (
        "what are neurons",
        "Neurons are specialized cells that transmit nerve signals."
    ),
    (
        "what is a nerve impulse",
        "A nerve impulse is an electrical signal that travels through neurons."
    ),
    (
        "what are sensory neurons",
        "Sensory neurons carry information from sense organs to the brain and spinal cord."
    ),
    (
        "what are motor neurons",
        "Motor neurons carry commands from the brain and spinal cord to muscles."
    ),
    (
        "what is a synapse",
        "A synapse is the point of communication between two neurons."
    ),
    (
        "what are reflexes",
        "Reflexes are fast, automatic responses to stimuli."
    ),

    # =====================================================
    # CIRCULATORY SYSTEM
    # =====================================================
    (
        "what is the circulatory system",
        "The circulatory system transports blood, oxygen, and nutrients throughout the body."
    ),
    (
        "what are the organs of the circulatory system",
        "The main organs of the circulatory system are the heart and blood vessels."
    ),
    (
        "what is the heart",
        "The heart is a muscular organ that pumps blood throughout the body."
    ),
    (
        "what are arteries",
        "Arteries carry blood away from the heart."
    ),
    (
        "what are veins",
        "Veins carry blood back to the heart."
    ),
    (
        "what are capillaries",
        "Capillaries are tiny blood vessels where substances are exchanged with cells."
    ),
    (
        "what is blood",
        "Blood is a liquid tissue that transports oxygen, nutrients, and waste products."
    ),
    (
        "what are the components of blood",
        "Blood is made of plasma, red blood cells, white blood cells, and platelets."
    ),
    (
        "what do red blood cells do",
        "Red blood cells carry oxygen to the body's tissues."
    ),
    (
        "what do white blood cells do",
        "White blood cells protect the body from germs and disease."
    ),
    (
        "what do platelets do",
        "Platelets help the blood clot."
    ),
    (
        "what is pulmonary circulation",
        "Pulmonary circulation carries blood from the heart to the lungs and back."
    ),
    (
        "what is systemic circulation",
        "Systemic circulation carries blood from the heart to the rest of the body and back."
    ),
    (
        "what is blood pressure",
        "Blood pressure is the force of blood pushing against the walls of blood vessels."
    ),
    (
        "how many chambers does the heart have",
        "The heart has four chambers: two atria and two ventricles."
    ),

    # =====================================================
    # QUIZ / HELP
    # =====================================================
    (
        "give me a biology quiz",
        "🧠 First question: Which organelle is known as the powerhouse of the cell?"
    ),
    (
        "give me a quiz about the nervous system",
        "🧠 Quiz! Which organ belongs to the central nervous system?"
    ),
    (
        "give me a quiz about the circulatory system",
        "❤️ Quiz! Which blood vessels carry blood away from the heart?"
    ),
    (
        "help me study biology",
        "Of course! 📚 I can help you study the nervous system, circulatory system, cells, DNA, genetics, and more."
    ),
    (
        "thank you thanks",
        "You're welcome 😊 Keep studying and exploring biology!"
    ),
]

THRESHOLD = 0.34


def normalize_text(text: str) -> str:
    """Converts text into a simpler form for better matching."""
    text = text.lower().strip()
    text = ''.join(
        char for char in unicodedata.normalize('NFD', text)
        if unicodedata.category(char) != 'Mn'
    )
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text


def similarity(a: str, b: str) -> float:
    a = normalize_text(a)
    b = normalize_text(b)

    seq_score = SequenceMatcher(None, a, b).ratio()

    words_a = set(a.split())
    words_b = set(b.split())
    if not words_a or not words_b:
        overlap_score = 0.0
    else:
        overlap_score = len(words_a & words_b) / len(words_a | words_b)

    return max(seq_score, overlap_score)


def get_response(user_input: str):
    best_score = 0.0
    best_answer = None

    for question, answer in qa_pairs:
        score = similarity(user_input, question)
        if score > best_score:
            best_score = score
            best_answer = answer

    if best_score < THRESHOLD:
        return best_score, (
            "I'm not sure I understood. Try asking something about biology, cells, DNA, "
            "the nervous system, the circulatory system, or photosynthesis."
        )

    return best_score, best_answer


class ChatbotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🧬 AI Biology Tutor")
        self.root.geometry("640x720")
        self.root.minsize(560, 620)
        self.root.configure(bg="#DEC5E3")

        self.bg_color = "#DEC5E3"
        self.chat_color = "#C2EABA"
        self.text_color = "#243025"
        self.accent_color = "#6B4E71"
        self.button_color = "#4F7B58"
        self.button_hover = "#3F6648"
        self.clear_color = "#B55A6A"

        main_frame = tk.Frame(root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=24, pady=22)

        header = tk.Frame(main_frame, bg=self.bg_color)
        header.pack(fill=tk.X, pady=(0, 14))

        tk.Label(
            header,
            text="🧬 AI Biology Tutor",
            font=("Helvetica", 24, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Your personal chatbox for studying Biology",
            font=("Helvetica", 11),
            fg="#5D4A61",
            bg=self.bg_color,
        ).pack(anchor="w", pady=(3, 0))

        chat_frame = tk.Frame(main_frame, bg=self.chat_color, bd=0, highlightthickness=0)
        chat_frame.pack(fill=tk.BOTH, expand=True)

        self.chat_area = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            font=("Arial", 12),
            bg=self.chat_color,
            fg=self.text_color,
            insertbackground=self.text_color,
            relief=tk.FLAT,
            bd=0,
            padx=18,
            pady=16,
        )
        self.chat_area.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)

        self.chat_area.tag_config("bot_name", foreground=self.accent_color, font=("Arial", 11, "bold"))
        self.chat_area.tag_config("user_name", foreground="#2F6F4E", font=("Arial", 11, "bold"), justify="right")
        self.chat_area.tag_config("bot_msg", foreground=self.text_color, spacing3=8, lmargin1=8, lmargin2=8)
        self.chat_area.tag_config("user_msg", foreground="#1F3D2B", spacing3=8, justify="right", rmargin=8)
        self.chat_area.tag_config("intro", foreground="#3D4A3E", spacing3=6)

        self.add_intro_message()
        self.chat_area.config(state="disabled")

        input_frame = tk.Frame(main_frame, bg=self.bg_color)
        input_frame.pack(fill=tk.X, pady=(16, 0))

        self.input_field = tk.Entry(
            input_frame,
            font=("Arial", 13),
            bg="#F7FFF5",
            fg=self.text_color,
            insertbackground=self.text_color,
            relief=tk.FLAT,
            bd=0,
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=12, padx=(0, 10))
        self.input_field.bind("<Return>", self.send_message)
        self.input_field.focus()

        self.send_button = tk.Button(
            input_frame,
            text="Send",
            command=self.send_message,
            font=("Arial", 12, "bold"),
            bg=self.button_color,
            fg="#FFFFFF",
            activebackground=self.button_hover,
            activeforeground="#FFFFFF",
            relief=tk.FLAT,
            bd=0,
            padx=18,
            pady=10,
            cursor="hand2",
        )
        self.send_button.pack(side=tk.LEFT)

        bottom_frame = tk.Frame(main_frame, bg=self.bg_color)
        bottom_frame.pack(fill=tk.X, pady=(12, 0))

        tk.Button(
            bottom_frame,
            text="Clear Chat",
            command=self.clear_chat,
            font=("Arial", 11, "bold"),
            bg=self.clear_color,
            fg="#FFFFFF",
            activebackground="#98495A",
            activeforeground="#FFFFFF",
            relief=tk.FLAT,
            bd=0,
            padx=14,
            pady=8,
            cursor="hand2",
        ).pack(anchor="e")

    def add_intro_message(self):
        self.chat_area.config(state="normal")
        self.chat_area.insert(
            tk.END,
            "🧬 AI Biology Tutor\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Hello! 👋\n\n"
            "I am a chatbot designed to help you study Biology.\n\n"
            "Ask me anything you want about Biology, and I will try to give you "
            "a simple, clear, and understandable answer.\n\n"
            "Type your question and let's begin! 😊\n\n",
            "intro"
        )
        self.chat_area.config(state="disabled")

    def add_message(self, sender: str, message: str, is_user=False):
        self.chat_area.config(state="normal")
        if is_user:
            self.chat_area.insert(tk.END, "\nYou\n", "user_name")
            self.chat_area.insert(tk.END, f"{message}\n", "user_msg")
        else:
            self.chat_area.insert(tk.END, "\nAI Biology Tutor\n", "bot_name")
            self.chat_area.insert(tk.END, f"{message}\n", "bot_msg")
        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)

    def send_message(self, event=None):
        user_input = self.input_field.get().strip()
        if not user_input:
            return

        score, response = get_response(user_input)
        self.add_message("You", user_input, is_user=True)
        self.add_message("AI Biology Tutor", response, is_user=False)
        # For debugging, uncomment the next line:
        # self.add_message("AI Biology Tutor", f"Match confidence: {score:.2f}")
        self.input_field.delete(0, tk.END)

    def clear_chat(self):
        self.chat_area.config(state="normal")
        self.chat_area.delete("1.0", tk.END)
        self.chat_area.config(state="disabled")
        self.add_intro_message()


def main():
    root = tk.Tk()
    ChatbotUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()