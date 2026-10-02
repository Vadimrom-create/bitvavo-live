# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T18:09:45.352597+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : BAT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.236 | entrée 6.100 | trend 8.700 | rang 7.731
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SPK-EUR | action LATENT_ACCELERATOR | opportunité 8.457 | entrée 5.600 | trend 9.200 | rang 7.946
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FLUID-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.286 | entrée 6.950 | trend 8.800 | rang 7.968
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.968
2. SPK-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.946
3. ALGO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.831

## Accélération indépendante

- BILL-EUR — BUILDING_ACCELERATION — score 5.251/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CVX-EUR — BUILDING_ACCELERATION — score 5.212/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — BUILDING_ACCELERATION — score 5.108/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 8.954/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — MEMORY_24H — score mémoire 8.283/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.145/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.968/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SPK-EUR — ACTIVE_NOW — score mémoire 7.946/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- GTC-EUR +57.75% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SAND-EUR +42.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SCR-EUR +19.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENJ-EUR +14.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +14.20% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- WLD-EUR +12.99% — DETECTED_EARLY — couche NONE — action NONE
- ATH-EUR +11.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKY-EUR +11.56% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- APE-EUR +11.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +10.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
