# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T13:29:47.376153+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 8.736 | entrée 7.350 | trend 8.400 | rang 7.771
  - V4 buy-ready with acceptable current entry; no structural veto. High extension/chase is retained as risk context, not an automatic veto.
- **MEILLEURE_LIMITE_PASSIVE** : 0G-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.288 | entrée 6.100 | trend 8.150 | rang 7.620
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : HUMA-EUR | action LATENT_ACCELERATOR | opportunité 7.699 | entrée 5.750 | trend 8.650 | rang 7.563
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MON-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.072 | entrée 6.400 | trend 8.550 | rang 8.101
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 7.771 — opportunité 8.736 — entrée 7.350 — trend 8.400
2. PUMP-EUR — ACHETE_MAINTENANT — rank 7.765 — opportunité 9.171 — entrée 7.100 — trend 7.800
3. SUI-EUR — ACHETE_MAINTENANT — rank 7.234 — opportunité 8.825 — entrée 7.600 — trend 6.150
4. ICP-EUR — ACHETE_MAINTENANT — rank 7.213 — opportunité 8.776 — entrée 7.050 — trend 6.500

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. MON-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.101
2. NOM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.843
3. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.828

## Accélération indépendante

- CAP-EUR — CONFIRMED_ACCELERATION — score 9.289/10 — DETECTED_BUT_TOO_LATE
- XMN-EUR — CONFIRMED_ACCELERATION — score 7.747/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SYN-EUR — CONFIRMED_ACCELERATION — score 7.334/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MON-EUR — CONFIRMED_ACCELERATION — score 6.635/10 — DETECTED_BUT_TOO_LATE
- ETHFI-EUR — BUILDING_ACCELERATION — score 5.721/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — BUILDING_ACCELERATION — score 4.891/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 9.573/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CAP-EUR — ACTIVE_NOW — score mémoire 9.289/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.740/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.257/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OSMO-EUR — MEMORY_DECAY_24_72H — score mémoire 8.193/10 — sources ACCELERATION — MEMORY_ONLY
- MON-EUR — ACTIVE_NOW — score mémoire 8.101/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SAND-EUR — MEMORY_24H — score mémoire 8.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAND-EUR +60.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +27.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ENJ-EUR +27.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +23.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +18.74% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GALA-EUR +18.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +17.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKY-EUR +16.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +14.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SPK-EUR +14.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
