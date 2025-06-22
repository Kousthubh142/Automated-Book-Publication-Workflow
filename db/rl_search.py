import json
from collections import defaultdict
import os

# In-memory Q-table (or loaded from disk)
RL_STATE_FILE = "db/rl_feedback.json"

if os.path.exists(RL_STATE_FILE):
    with open(RL_STATE_FILE, "r") as f:
        q_table = json.load(f)
else:
    q_table = defaultdict(lambda: 0.0)

def reward_version(doc_id: str, reward: float = 1.0):
    """
    Increases Q-value for a document based on positive feedback.
    """
    q_table[doc_id] = q_table.get(doc_id, 0.0) + reward
    _save_q_table()

def penalize_version(doc_id: str, penalty: float = 1.0):
    """
    Decreases Q-value for a document based on negative feedback.
    """
    q_table[doc_id] = q_table.get(doc_id, 0.0) - penalty
    _save_q_table()

def get_ranked_versions(doc_ids: list[str]) -> list[str]:
    """
    Sorts given document IDs based on RL-learned relevance scores.
    """
    return sorted(doc_ids, key=lambda x: q_table.get(x, 0.0), reverse=True)

def _save_q_table():
    with open(RL_STATE_FILE, "w") as f:
        json.dump(q_table, f, indent=2)
