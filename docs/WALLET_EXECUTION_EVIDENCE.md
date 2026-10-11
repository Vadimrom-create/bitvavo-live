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

**Restitution confidentielle WALLET -> Gmail :** le workflow `private_wallet_refresh.yml`
génère et enrichit le résumé en lecture seule, vérifie les données, puis exécute
`scripts/email_private_wallet_summary.py` **avant** de chiffrer et de supprimer le
fichier clair local. L'email est envoyé uniquement à la boîte autorisée
`bellonirom@gmail.com`, via la configuration `ALERT_GMAIL_USER` et le secret
`GMAIL_APP_PASSWORD` existants ; aucun nouveau token Bitvavo ou Gmail n'est
nécessaire. Seuls les totaux, les positions, les PRU reconstruits, les PnL
**bruts estimés**, et les résumés agrégés des carnets/trades sont inclus.
Les prix et preuves de marché trop anciens sont explicitement déclassés ;
le résumé de compte lui-même n'est envoyé que s'il a au plus 180 secondes.
Aucune clé, aucun détail de portefeuille et aucun corps d'email ne sont
inscrits dans les logs, Git, les artefacts publics ou les résumés d'étape.

Le flux émet **un email par cycle de cinq minutes**, jusqu'à environ
288 messages/jour tant qu'il fonctionne continuellement. Pour éviter les
notifications, configurer dans Gmail un filtre sur l'objet exact
`SOLAIRE WALLET — relevé privé` et ignorer la boîte de réception.
Les emails sont un moyen de restitution distinct de la publication GitHub :
ce n'est **pas** une synchronisation temps réel native avec ChatGPT.
À chaque demande WALLET, ChatGPT peut chercher le dernier email et vérifier
son horodatage ; s'il est trop ancien, il doit refuser de qualifier les
cours d'« instantanés ». L'accès à Gmail connecté reste nécessaire.

Dans un dépôt public, les artefacts GitHub restent obligatoirement chiffrés.
Ne jamais communiquer `POSITION_STATE_KEY` ni les secrets SMTP dans un chat.
Si l'envoi Gmail est indisponible, le workflow continue la publication chiffrée
et le prochain heartbeat ; l'étape d'envoi apparaît toutefois en erreur
(`PRIVATE_WALLET_EMAIL_...` sans données privées dans le log).

Supprimer un artifact limite les accès futurs ; cela ne révoque pas les copies
éventuellement téléchargées auparavant.

Aucun endpoint Bitvavo privé supplémentaire, aucun ordre et
aucune modification de la politique stop-loss. Seul l'email privé WALLET a été ajouté. Le scanner public, les
fichiers utilisés pour ses alertes d'achat et `execution_snapshot.json`
restent indépendants. Les champs de freshness doivent être recontrôlés au
moment de chaque réponse utilisateur ; un artifact de la nuit ne peut être
présenté comme une cotation instantanée en journée.
