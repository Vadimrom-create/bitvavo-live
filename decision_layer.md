# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T21:20:13.428302+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XLM-EUR | action ACHETE_MAINTENANT | opportunité 7.857 | entrée 7.350 | trend 8.700 | rang 7.868
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MMT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.522 | entrée 6.150 | trend 8.750 | rang 7.545
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : RED-EUR | action LATENT_ACCELERATOR | opportunité 8.339 | entrée 5.650 | trend 9.200 | rang 7.929
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KSM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.893 | entrée 6.900 | trend 9.200 | rang 7.936
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. XLM-EUR — ACHETE_MAINTENANT — rank 7.868 — opportunité 7.857 — entrée 7.350 — trend 8.700

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KSM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.936
2. RED-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.929
3. ZRO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.876

## Accélération indépendante

- LMWR-EUR — CONFIRMED_ACCELERATION — score 9.685/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — CONFIRMED_ACCELERATION — score 6.889/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PHA-EUR — CONFIRMED_ACCELERATION — score 6.602/10 — DETECTED_BUT_TOO_LATE
- MON-EUR — BUILDING_ACCELERATION — score 6.331/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — BUILDING_ACCELERATION — score 6.120/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LMWR-EUR — ACTIVE_NOW — score mémoire 9.685/10 — sources ACCELERATION, V4 — WATCH_ONLY
- CT-EUR — MEMORY_24H — score mémoire 9.221/10 — sources ACCELERATION — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DGB-EUR — MEMORY_24H — score mémoire 8.670/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARPA-EUR — MEMORY_24H — score mémoire 8.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 8.565/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVR-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.214/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- MOVR-EUR +59.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +46.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +19.18% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- SOON-EUR +17.63% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +16.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CAP-EUR +13.82% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AUDIO-EUR +13.59% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- STX-EUR +12.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +12.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TRAC-EUR +11.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
