# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-02T11:38:52.361687+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : WLD-EUR | action ACHETE_MAINTENANT | opportunité 9.339 | entrée 7.850 | trend 8.700 | rang 8.575
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : BRETT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.060 | entrée 6.100 | trend 8.250 | rang 7.587
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : DYDX-EUR | action LATENT_ACCELERATOR | opportunité 8.278 | entrée 5.100 | trend 8.950 | rang 7.806
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HUMA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.138 | entrée 5.600 | trend 8.850 | rang 7.841
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. WLD-EUR — ACHETE_MAINTENANT — rank 8.575 — opportunité 9.339 — entrée 7.850 — trend 8.700
2. LINK-EUR — ACHETE_MAINTENANT — rank 7.324 — opportunité 8.821 — entrée 7.650 — trend 6.450
3. EIGEN-EUR — ACHETE_MAINTENANT — rank 7.018 — opportunité 8.141 — entrée 7.050 — trend 6.350

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.575
2. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.841
3. DYDX-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.806

## Accélération indépendante

- QNT-EUR — BUILDING_ACCELERATION — score 5.588/10 — DETECTED_BUT_TOO_LATE
- MERL-EUR — BUILDING_ACCELERATION — score 5.385/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SIGN-EUR — BUILDING_ACCELERATION — score 5.236/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LQTY-EUR — BUILDING_ACCELERATION — score 5.218/10 — DETECTED_BUT_TOO_LATE
- GALA-EUR — BUILDING_ACCELERATION — score 5.215/10 — DETECTED_BUT_TOO_LATE
- SAND-EUR — BUILDING_ACCELERATION — score 5.045/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 9.258/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 9.112/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 8.740/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.575/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.257/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 7.987/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SAND-EUR +56.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GTC-EUR +29.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +21.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +19.64% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SCR-EUR +18.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKY-EUR +16.66% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MAGIC-EUR +15.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SUPER-EUR +14.15% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ZK-EUR +13.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +12.66% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
