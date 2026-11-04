# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-04T22:15:50.781704+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ICNT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.080 | entrée 6.650 | trend 7.750 | rang 6.678
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ICNT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.678
2. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.359

## Accélération indépendante

- ADX-EUR — CONFIRMED_ACCELERATION — score 9.096/10 — DETECTED_BUT_TOO_LATE
- CHILLGUY-EUR — CONFIRMED_ACCELERATION — score 8.951/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BREV-EUR — CONFIRMED_ACCELERATION — score 7.995/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- JTO-EUR — CONFIRMED_ACCELERATION — score 7.710/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BAT-EUR — CONFIRMED_ACCELERATION — score 7.164/10 — DETECTED_BUT_TOO_LATE
- XMN-EUR — CONFIRMED_ACCELERATION — score 6.972/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — CONFIRMED_ACCELERATION — score 6.799/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.696/10 — DETECTED_BUT_TOO_LATE
- MANTA-EUR — BUILDING_ACCELERATION — score 5.677/10 — DETECTED_BUT_TOO_LATE
- MANTRA-EUR — BUILDING_ACCELERATION — score 5.669/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PUFFER-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- ADX-EUR — ACTIVE_NOW — score mémoire 9.096/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- CHILLGUY-EUR — ACTIVE_NOW — score mémoire 8.951/10 — sources ACCELERATION — WATCH_ONLY
- AXIS-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- KMNO-EUR — MEMORY_24H — score mémoire 8.560/10 — sources ACCELERATION — MEMORY_ONLY
- RUNE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.067/10 — sources ACCELERATION — MEMORY_ONLY
- BREV-EUR — ACTIVE_NOW — score mémoire 7.995/10 — sources ACCELERATION — WATCH_ONLY
- NOS-EUR — MEMORY_24H — score mémoire 7.864/10 — sources ACCELERATION — MEMORY_ONLY
- JTO-EUR — ACTIVE_NOW — score mémoire 7.710/10 — sources ACCELERATION — WATCH_ONLY
- BAT-EUR — ACTIVE_NOW — score mémoire 7.164/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ELSA-EUR +71.05% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +27.25% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IKA-EUR +25.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUID-EUR +22.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BAT-EUR +14.42% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NOS-EUR +14.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +13.53% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PTB-EUR +13.45% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRUST-EUR +13.10% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- USELESS-EUR +11.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
