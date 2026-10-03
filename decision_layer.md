# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T10:38:28.404557+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.380 | entrée 7.900 | trend 8.900 | rang 8.194
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : FLUID-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.965 | entrée 5.900 | trend 9.000 | rang 7.845
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 8.008 | entrée 4.750 | trend 9.200 | rang 7.789
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GALA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.734 | entrée 6.550 | trend 8.650 | rang 7.698
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. AAVE-EUR — ACHETE_MAINTENANT — rank 8.194 — opportunité 8.380 — entrée 7.900 — trend 8.900
2. ATH-EUR — ACHETE_MAINTENANT — rank 7.748 — opportunité 8.739 — entrée 7.550 — trend 9.000
3. SYRUP-EUR — ACHETE_MAINTENANT — rank 7.465 — opportunité 8.207 — entrée 7.000 — trend 7.600
4. RENDER-EUR — ACHETE_MAINTENANT — rank 7.383 — opportunité 8.889 — entrée 7.450 — trend 6.550
5. ONDO-EUR — ACHETE_MAINTENANT — rank 7.113 — opportunité 8.767 — entrée 7.700 — trend 5.900
6. SUI-EUR — ACHETE_MAINTENANT — rank 7.005 — opportunité 8.141 — entrée 7.150 — trend 6.300
7. FET-EUR — ACHETE_MAINTENANT — rank 6.971 — opportunité 8.743 — entrée 7.400 — trend 5.850
8. AVAX-EUR — ACHETE_MAINTENANT — rank 6.491 — opportunité 7.404 — entrée 7.200 — trend 6.050
9. VIRTUAL-EUR — ACHETE_MAINTENANT — rank 6.143 — opportunité 8.484 — entrée 7.100 — trend 5.050

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.194
2. FLUID-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.845
3. IMX-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.789

## Accélération indépendante

- AGI-EUR — CONFIRMED_ACCELERATION — score 8.789/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — CONFIRMED_ACCELERATION — score 8.500/10 — DETECTED_BUT_TOO_LATE
- DYDX-EUR — CONFIRMED_ACCELERATION — score 6.551/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- UP-EUR — BUILDING_ACCELERATION — score 5.738/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — BUILDING_ACCELERATION — score 5.500/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ATH-EUR — ACTIVE_NOW — score mémoire 7.748/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- FET-EUR — ACTIVE_NOW — score mémoire 6.971/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.831/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AGI-EUR — ACTIVE_NOW — score mémoire 8.789/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PEOPLE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.716/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- USELESS-EUR — ACTIVE_NOW — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.194/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.048/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- HFT-EUR +26.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SAND-EUR +14.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ATH-EUR +13.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +12.14% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- WLD-EUR +11.78% — DETECTED_EARLY — couche NONE — action NONE
- FOLD-EUR +11.70% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- QNT-EUR +11.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUPER-EUR +7.51% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- INIT-EUR +7.43% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GRASS-EUR +6.69% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
