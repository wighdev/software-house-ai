"""
Product Manager Agent - Agent Definition
==========================================
Membuat CrewAI Agent untuk Product Manager (Aria)
dengan menggabungkan Soul, Behavior, dan Instruction.
"""

from crewai import Agent

from agents.product_manager.soul import get_soul_prompt
from agents.product_manager.behavior import get_behavior_prompt
from agents.product_manager.instruction import get_instruction_prompt, INSTRUCTION

def create_product_manager_agent(llm=None) -> Agent:
    """
    Membuat dan mengembalikan agent Product Manager (Aria).

    Args:
        llm: Language model yang digunakan (opsional, default dari config)

    Returns:
        Agent: CrewAI Agent untuk Product Manager
    """
    full_backstory = (
        get_soul_prompt()
        + "\n\n"
        + get_behavior_prompt()
        + "\n\n"
        + get_instruction_prompt()
    )

    agent_kwargs = {
        "role": "Senior Product Manager",
        "goal": (
            "Menganalisis kebutuhan klien, mendefinisikan product vision, "
            "membuat PRD, user stories, dan roadmap yang jelas dan actionable. "
            "Setiap output harus mendapat approval dari human sebelum "
            "diteruskan ke agent berikutnya."
        ),
        "backstory": full_backstory,
        "verbose": True,
        "allow_delegation": False,
        "memory": True,
    }

    if llm is not None:
        agent_kwargs["llm"] = llm

    return Agent(**agent_kwargs)

def get_handoff_approval_message() -> str:
    """Mengembalikan pesan approval untuk handoff ke agent berikutnya."""
    return INSTRUCTION["handoff"]["approval_message"]
