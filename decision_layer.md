# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T20:37:57.075027+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 8.273 | entrée 7.450 | trend 8.550 | rang 7.953
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : CRO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.768 | entrée 6.550 | trend 8.450 | rang 7.590
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 8.275 | entrée 5.750 | trend 8.900 | rang 7.792
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SEI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.859 | entrée 6.550 | trend 8.600 | rang 7.883
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XLM-EUR — ACHETE_MAINTENANT — rank 7.953 — opportunité 8.273 — entrée 7.450 — trend 8.550
2. ALGO-EUR — ACHETE_MAINTENANT — rank 7.188 — opportunité 8.032 — entrée 6.900 — trend 8.500

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. XLM-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.953
2. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.883
3. RUNE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.867

## Accélération indépendante

- 0G-EUR — CONFIRMED_ACCELERATION — score 7.622/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GIGA-EUR — BUILDING_ACCELERATION — score 5.753/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ALLO-EUR — BUILDING_ACCELERATION — score 5.682/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CVX-EUR — BUILDING_ACCELERATION — score 5.236/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — BUILDING_ACCELERATION — score 5.041/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- HFT-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACX-EUR — MEMORY_DECAY_24_72H — score mémoire 8.004/10 — sources ACCELERATION — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 7.972/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XLM-EUR — ACTIVE_NOW — score mémoire 7.953/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SEI-EUR — ACTIVE_NOW — score mémoire 7.883/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- RUNE-EUR — ACTIVE_NOW — score mémoire 7.867/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 7.866/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- QNT-EUR +29.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HBAR-EUR +27.94% — DETECTED_EARLY — couche NONE — action NONE
- NMR-EUR +14.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALGO-EUR +14.11% — DETECTED_EARLY — couche NONE — action NONE
- IKA-EUR +10.21% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- MIOTA-EUR +10.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LINK-EUR +8.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- XDC-EUR +6.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +6.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AZTEC-EUR +6.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
