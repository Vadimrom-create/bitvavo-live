# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T19:27:25.889006+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : GALA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.984 | entrée 5.800 | trend 8.700 | rang 7.647
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : SPK-EUR | action LATENT_ACCELERATOR | opportunité 7.749 | entrée 5.450 | trend 8.550 | rang 7.457
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HUMA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.272 | entrée 6.050 | trend 8.550 | rang 8.276
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.276
2. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.892
3. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.750

## Accélération indépendante

- GTC-EUR — BUILDING_ACCELERATION — score 5.950/10 — DETECTED_BUT_TOO_LATE
- LRC-EUR — BUILDING_ACCELERATION — score 4.921/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 8.954/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- HUMA-EUR — ACTIVE_NOW — score mémoire 8.276/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 7.820/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.750/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +38.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +36.47% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ATH-EUR +14.33% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENJ-EUR +13.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SCR-EUR +13.62% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +10.02% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- VVV-EUR +9.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CT-EUR +9.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APE-EUR +8.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WLD-EUR +8.62% — DETECTED_EARLY — couche NONE — action NONE

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
