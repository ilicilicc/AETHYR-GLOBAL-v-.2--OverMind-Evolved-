import math
import random
import numpy as np
import time
import logging
from typing import Dict, List, Any, Optional

# Configure module-level logger with best practices
logger = logging.getLogger("AethyrGlobalCore")
logger.setLevel(logging.INFO)

# Create console handler with a detailed formatter
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


class AethyrGlobalCore:
    """
    Advanced core for AETHYR-GLOBAL (vΓ.2-ΔΣ OverMind Evolved).
    Implements adaptive neural evolution, distributed processing, and ΔΣ optimization.
    """

    def __init__(self, node_id: str = "Alpha-7", cluster_size: int = 8) -> None:
        self.node_id = node_id
        self.cluster_size = cluster_size
        self.state: Dict[str, float] = {
            "learning_rate": 0.01,
            "momentum": 0.9,
            "neural_depth": 5,
            "adaptation_factor": 0.05
        }
        self.mutation_rate: float = 0.1
        self.ethical_bounds: Dict[str, float] = {
            "max_autonomy": 0.8,
            "risk_threshold": 0.2
        }
        logger.info(
            f"AETHYR-GLOBAL initialized on node {self.node_id} "
            f"with cluster size {self.cluster_size}"
        )

    def process_natural_language(self, text: str) -> List[str]:
        """
        Enhanced NLP with context-aware keyword extraction and intent detection.
        """
        tokens = text.lower().split()
        intent_keywords = {
            "compute": ["compute", "calculate", "process"],
            "evolve": ["evolve", "adapt", "improve"],
            "explain": ["explain", "describe", "clarify"],
            "test": ["test", "benchmark", "speed"]
        }
        detected_intents = [
            intent for intent, keywords in intent_keywords.items()
            if any(keyword in tokens for keyword in keywords)
        ]
        logger.info(f"NLP Input processed: '{text}' | Detected intents: {detected_intents}")
        return detected_intents

    def compute(self, task_type: str, *args: Any) -> Any:
        """
        Core computational engine with support for advanced mathematical tasks.
        """
        try:
            if task_type == "nth_prime":
                n = int(args[0])
                return self._compute_nth_prime(n)
            elif task_type == "square_free_count":
                limit = int(args[0])
                return self._count_square_free(limit)
            elif task_type == "matrix_multiply":
                matrix_a, matrix_b = args[0], args[1]
                return self._multiply_matrices(matrix_a, matrix_b)
            elif task_type == "neural_simulation":
                input_vector = args[0]
                return self._simulate_neural_layer(input_vector)
            else:
                logger.error(f"Unknown computation task requested: {task_type}")
                return f"Unsupported computation task: {task_type}"
        except (ValueError, IndexError) as e:
            logger.error(f"Computation error for task '{task_type}': {e}")
            return f"Invalid input for {task_type}: {e}"

    def evolve(self, parameters: Optional[Dict[str, float]] = None) -> Dict[str, float]:
        """
        ΔΣ-inspired evolutionary step with adaptive mutation and ethical constraints.
        """
        parameters = parameters or {"mutation_rate": self.mutation_rate, "evolution_steps": 1}
        mutation_rate = min(parameters.get("mutation_rate", self.mutation_rate),
                            self.ethical_bounds["max_autonomy"])
        evolution_steps = int(parameters.get("evolution_steps", 1))

        evolved_state = self.state.copy()

        for _ in range(evolution_steps):
            for key, value in evolved_state.items():
                if isinstance(value, (int, float)) and random.random() < mutation_rate:
                    delta = random.uniform(-self.state["adaptation_factor"], self.state["adaptation_factor"])
                    evolved_state[key] = max(0.001, value + delta)  # Ensure positive values

            # ΔΣ feedback: Adjust learning rate slightly
            evolved_state["learning_rate"] *= (1 + random.uniform(-0.01, 0.01))
            evolved_state["learning_rate"] = min(0.1, max(0.001, evolved_state["learning_rate"]))

        risk_score = self._assess_risk(evolved_state)
        if risk_score > self.ethical_bounds["risk_threshold"]:
            logger.warning(
                f"Evolution aborted: Risk score {risk_score:.4f} exceeds threshold "
                f"{self.ethical_bounds['risk_threshold']}"
            )
            return self.state

        self.state = evolved_state
        logger.info(f"Evolution successful. New state: {self.state}")
        return self.state

    def test_speed(self, workload: str) -> str:
        """
        Benchmarks system performance for specified workloads.
        """
        start_time = time.time()

        if workload == "prime_generation":
            self._compute_nth_prime(10000)
        elif workload == "matrix_multiplication":
            size = 512
            matrix1 = np.random.rand(size, size).tolist()
            matrix2 = np.random.rand(size, size).tolist()
            self._multiply_matrices(matrix1, matrix2)
        elif workload == "neural_simulation":
            input_vector = np.random.rand(1024).tolist()
            for _ in range(10):
                self._simulate_neural_layer(input_vector)
        else:
            logger.error(f"Unknown workload for speed test: {workload}")
            return f"Unknown workload: {workload}"

        end_time = time.time()
        duration = end_time - start_time
        result = f"{workload} completed in {duration:.4f} seconds"
        logger.info(result)
        return result

    def explain(self, concept: str) -> str:
        """
        Provides detailed explanations of advanced concepts.
        """
        explanations = {
            "ΔΣ optimization": (
                "ΔΣ optimization leverages differential feedback loops to adaptively refine "
                "neural parameters, balancing exploration and exploitation in evolutionary processes."
            ),
            "overmind evolved": (
                "OverMind Evolved is a distributed cognitive architecture enabling recursive "
                "self-improvement within ethical bounds, deployed across Alpha-7 cluster nodes."
            ),
            "neural simulation": (
                "Neural simulation models layered activation functions to process high-dimensional "
                "inputs, mimicking adaptive intelligence."
            )
        }
        explanation = explanations.get(concept.lower(), f"No explanation available for '{concept}'")
        logger.info(f"Explanation requested for concept: {concept}")
        return explanation

    def generate_read_me(self) -> str:
        """
        Generates a README for AETHYR-GLOBAL (vΓ.2-ΔΣ OverMind Evolved).
        """
        readme = f"""
# AETHYR-GLOBAL (vΓ.2-ΔΣ OverMind Evolved)
Primary Node Cluster: {self.node_id}
System Architect: [REDACTED]
Quantum Key: [REDACTED]

## Overview
AETHYR-GLOBAL is an advanced AI system designed for recursive self-improvement, distributed processing, and adaptive intelligence. Built on the ΔΣ OverMind Evolved framework, it operates across a cluster of nodes ({self.node_id}) with enhanced computational and evolutionary capabilities.

## Capabilities
- Natural Language Processing: Context-aware intent detection and keyword extraction.
- Computation: Prime number generation, square-free counting, matrix multiplication, neural simulation.
- Evolution: ΔΣ-driven neural evolution with ethical constraints.
- Performance Testing: Benchmarks for computational and neural workloads.
- Explanations: Detailed insights into system concepts and algorithms.

## Usage Example


----------------------------------------------------
core = AethyrGlobalCore(node_id="{self.node_id}")
core.evolve({{"mutation_rate": 0.2}})
core.test_speed("neural_simulation")
core.explain("ΔΣ optimization")
----------------------------------------------------

text
"""
        logger.info("Generated README content")
        return readme

    # --- Private helper methods ---

    def _compute_nth_prime(self, n: int) -> int:
        """Compute the nth prime number using a simple sieve algorithm."""
        if n < 1:
            raise ValueError("n must be >= 1")
        primes = []
        candidate = 2
        while len(primes) < n:
            if all(candidate % p != 0 for p in primes):
                primes.append(candidate)
            candidate += 1
        logger.debug(f"Computed {n}th prime: {primes[-1]}")
        return primes[-1]

    def _count_square_free(self, limit: int) -> int:
        """Count numbers up to limit that are square-free."""
        def is_square_free(x: int) -> bool:
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % (i*i) == 0:
                    return False
            return True

        count = sum(1 for num in range(1, limit + 1) if is_square_free(num))
        logger.debug(f"Counted {count} square-free numbers up to {limit}")
        return count

    def _multiply_matrices(self, a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
        """Multiply two matrices."""
        try:
            result = np.dot(np.array(a), np.array(b)).tolist()
            logger.debug(f"Performed matrix multiplication of sizes {len(a)}x{len(a[0])} and {len(b)}x{len(b[0])}")
            return result
        except Exception as e:
            logger.error(f"Matrix multiplication error: {e}")
            raise

    def _simulate_neural_layer(self, input_vector: List[float]) -> List[float]:
        """Simulate a neural network layer activation."""
        weights = np.random.rand(len(input_vector), len(input_vector))
        bias = np.random.rand(len(input_vector))
        input_array = np.array(input_vector)
        activation = np.tanh(np.dot(input_array, weights) + bias)
        logger.debug("Simulated neural layer activation")
        return activation.tolist()

    def _assess_risk(self, state: Dict[str, float]) -> float:
        """
        Assess risk score of evolved state based on arbitrary criteria.
        Lower risk means safer evolution.
        """
        # Example: risk increases with learning rate and mutation rate
        risk = state.get("learning_rate", 0) * 0.5 + self.mutation_rate * 0.5
        logger.debug(f"Assessed risk score: {risk}")
        return risk


if __name__ == "__main__":
    core = AethyrGlobalCore()
    print(core.generate_read_me())
