"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                           YOUR TASK PROMPTS                                   ║
║                                                                               ║
║  CUSTOMIZE THIS FILE to define prompts/instructions for your task.            ║
║  Prompts are selected based on task type and returned to the model.           ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import random


# ══════════════════════════════════════════════════════════════════════════════
#  DEFINE YOUR PROMPTS
# ══════════════════════════════════════════════════════════════════════════════

PROMPTS = {
    "default": [
        "Given the mirror reflectivity = {reflectivity:.2f}, predict the reflection of light when it hits the mirror. The reflected ray should extend to the edge of the image.",
        "Given the mirror reflectivity = {reflectivity:.2f}, predict how light reflects when it encounters the mirror. Extend the reflected ray to the image boundary.",
        "Given the mirror reflectivity = {reflectivity:.2f}, predict the light reflection from the mirror surface. The reflected ray must extend all the way to the edge of the image.",
    ],
}


def get_prompt(task_type: str = "default", task_data: dict = None) -> str:
    """
    Select a random prompt for the given task type.
    
    Args:
        task_type: Type of task (key in PROMPTS dict)
        task_data: Task data dictionary containing reflectivity
        
    Returns:
        Random prompt string from the specified type with reflectivity filled in
    """
    prompts = PROMPTS.get(task_type, PROMPTS["default"])
    prompt_template = random.choice(prompts)
    
    # Fill in the reflectivity if task_data is provided
    if task_data and "reflectivity" in task_data:
        return prompt_template.format(reflectivity=task_data["reflectivity"])
    else:
        # Fallback if no task_data provided
        return prompt_template.format(reflectivity=0.8)


def get_all_prompts(task_type: str = "default") -> list[str]:
    """Get all prompts for a given task type."""
    return PROMPTS.get(task_type, PROMPTS["default"])


# ══════════════════════════════════════════════════════════════════════════════
#  NOTE: This generator does not use rubrics
# ══════════════════════════════════════════════════════════════════════════════
#
# The TaskPair schema only includes:
#   - task_id, domain, prompt
#   - first_image, final_image  
#   - ground_truth_video (optional)
#
# No rubric field exists in the schema, so only prompts are generated.
# ══════════════════════════════════════════════════════════════════════════════
