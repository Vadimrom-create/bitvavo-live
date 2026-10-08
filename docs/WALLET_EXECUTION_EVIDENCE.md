# WALLET — collecte des carnets et transactions des positions détenues

## Fonctionnement

Le workflow `.github/workflows/private_wallet_refresh.yml` crée d'abord
`wallet_private_summary.json` depuis les soldes Bitvavo **en lecture seule**.
`scripts/enrich_private_wallet.py` charge ensuite ce résumé, découvre ses
`positions[*].market`, et interroge uniquement les API publiques Bitvavo
`/ticker/24h`, `/{market}/book?depth=100` et `/{market}/trades?limit=100`.

Aucune position détenue n'est exclue au motif qu'elle est absente de
`decision_watchlist.json`, du scanner Solaire, ou d'un classement V3/V4.
Chaque position reçoit `execution_evidence`, même si les observations sont
impossibles (`PARTIAL`, `UNAVAILABLE` ou `NOT_OBSERVED`). Les opérations
sont soumises à un budget de 90 secondes et 30 actifs par cycle :
l'absence de collecte est explicitement indiquée, jamais assimilée à un
carnet vide ni à une absence de détention.

## Mesures par position

- Carnet jusqu'à **100 bids + 100 asks**, meilleur bid/ask et tailles,
  spread recalculé depuis le **même carnet** et profondeur notionnelle
  à ±0,25 %, ±0,5 % et ±1 %.
- Jusqu'à **100 transactions publiques**, horodatage et prix du dernier
  échange, VWAP, volumes agressifs acheteur/vendeur, part acheteuse et
  durée de la fenêtre couverte par l'échantillon.
- Volume EUR 24 h, variation 24 h et dernier cours du ticker public.
- Estimation du prix moyen de vente **de la quantité réellement détenue**
  sur le carnet observé ; simulations distinctes d'achat et de vente de
  50/100/150 EUR, sans déduction de frais ni ordre exécuté.
- Horodatage propre du ticker, du carnet et des trades ; âges au moment de
  l'écriture. Une collecte de plus de 90 secondes ou un dernier trade
  datant de plus de 15 minutes ne reçoit **pas** le statut OK.

Les données sont des photographies ponctuelles, **pas** un historique des
ordres exécutés et non exécutés. Un gros mur bid peut être retiré ; un
échantillon de 100 trades ne prouve pas une tendance durable. Les simulations
de slippage ne tiennent pas compte de la profondeur future ni des frais réels.

## Confidentialité, accès et non-régression

Le fichier enrichi n'est jamais ajouté à Git, ni à
`execution_snapshot.json`, ni aux fichiers publics de détection. Les logs de
validation n'affichent ni montants ni symboles du wallet.

**Publication conditionnée à la visibilité GitHub :**

- **Dépôt public :** `scripts/protect_private_wallet_artifact.py` chiffre
  obligatoirement le résumé avec Fernet et la clé secrète `POSITION_STATE_KEY`
  déjà configurée ; il vérifie l'authenticité du chiffrement, efface le fichier
  en clair du workspace avant upload et publie uniquement
  `encrypted-wallet-summary-…`. Sans clé valide : aucune publication.
  Les anciens artifacts publics `private-wallet-summary-…` sont supprimés
  via API GitHub, avec la permission Actions write du workflow.
- **Dépôt privé :** publication en clair sous le nom historique
  `private-wallet-summary-…`, accessible aux lecteurs autorisés du dépôt.

**Conséquence fonctionnelle importante :** tant que le dépôt reste public, un
assistant sans la clé de déchiffrement ne peut pas lire automatiquement les
quantités et PRU à partir des futurs artifacts chiffrés. Il ne faut jamais
communiquer la clé dans un chat. Pour retrouver le mode WALLET connecté en
lecture directe sans exposer les soldes publiquement, rendre le dépôt GitHub
**privé** et confirmer que le connecteur GitHub y conserve son accès.

Supprimer un artifact limite les accès futurs ; cela ne révoque pas les copies
éventuellement téléchargées auparavant.

Aucun endpoint Bitvavo privé supplémentaire, aucun ordre, aucun email et
aucune modification de la politique stop-loss. Le scanner public, les
fichiers utilisés pour ses alertes d'achat et `execution_snapshot.json`
restent indépendants. Les champs de freshness doivent être recontrôlés au
moment de chaque réponse utilisateur ; un artifact de la nuit ne peut être
présenté comme une cotation instantanée en journée.
