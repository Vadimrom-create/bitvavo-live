# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T09:58:29.114160+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HBAR-EUR | action ACHETE_MAINTENANT | opportunité 9.236 | entrée 8.050 | trend 8.200 | rang 8.329
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : IMX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.198 | entrée 5.900 | trend 8.450 | rang 7.574
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DYDX-EUR | action LATENT_ACCELERATOR | opportunité 7.496 | entrée 5.750 | trend 8.950 | rang 7.551
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AAVE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.585 | entrée 7.400 | trend 8.900 | rang 7.787
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. HBAR-EUR — ACHETE_MAINTENANT — rank 8.329 — opportunité 9.236 — entrée 8.050 — trend 8.200
2. WLD-EUR — ACHETE_MAINTENANT — rank 8.008 — opportunité 8.605 — entrée 7.000 — trend 8.700

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. HBAR-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.329
2. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.008
3. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.787

## Accélération indépendante

- NEO-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- VVV-EUR — CONFIRMED_ACCELERATION — score 6.574/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDEN-EUR — BUILDING_ACCELERATION — score 5.813/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SCR-EUR — BUILDING_ACCELERATION — score 5.643/10 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — BUILDING_ACCELERATION — score 5.179/10 — DETECTED_BUT_TOO_LATE
- SLP-EUR — BUILDING_ACCELERATION — score 4.868/10 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — BUILDING_ACCELERATION — score 4.850/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 9.112/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- NEO-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- HBAR-EUR — ACTIVE_NOW — score mémoire 8.329/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.257/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.008/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 7.987/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SWEAT-EUR +179.99% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SAND-EUR +48.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +30.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +29.82% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SCR-EUR +19.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +17.12% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- MAGIC-EUR +15.51% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SKY-EUR +14.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +14.32% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZRO-EUR +14.30% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
