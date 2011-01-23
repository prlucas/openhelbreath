from Helpers import Struct

# Helbreath Packet definitions

RESPONSE_PLAYERDATA = Struct(
	(('char_name', '10s'),
	('account_status', 'x'), # Outdated?
	('guild_status', 'x'), # Outdated?
	('map_name', '10s'),
	('x', 'h'),
	('y', 'h'),
	('sex', 'B'),
	('skin', 'B'),
	('hair_style', 'B'),
	('hair_olor', 'B'),
	('underwear', 'B'),
	('guild_name', '20s'),
	('guild_rank', 'b'),
	('hp', 'I'),
	('level', 'H'),
	('str', 'B'),
	('vit', 'B'),
	('dex', 'B'),
	('int', 'B'),
	('mag', 'B'),
	('chr', 'B'),
	('luck', 'B'),
	('exp', 'I'),
	('magic_mastery', '100s'),
	('skill_mastery', '24s'),
	('location', '10s'),
	('mp', 'I'),
	('sp', 'I'),
	('lu_pool', 'x'),
	('ek_count', 'I'),
	('pk_count', 'I'),
	('reward_gold', 'I'),
	('skill_ssn', '96s'),
	('padding1', '4x'), # 
	('hunger_status', 'B'),
	('admin_user_level', 'B'),
	('timeleft_shutup', 'I'),
	('timeleft_rating', 'I'),
	('rating', 'i'),
	('guild_guid', 'i'),
	('down_skill_index', 'b'),
	('char_id', 'I'),
	('char_idnum1', 'I'),
	('char_idnum2', 'I'),
	('char_idnum3', 'I'),
	('block_date','20s'),
	('questnum','h'),
	('questcount','h'),
	('questrewtype','h'),
	('questrewammount','i'),
	('contribution','i'),
	('questid','i'),
	('questcompleted','B'),
	('leftforcerecalltime','i'),
	('leftfirmstaminartime','i'),
	('eventid','i'),
	('leftsac','h'),
	('fightnum','B'),
	('fightdate','i'),
	('fightticket','B'),
	('leftspecialtime','i'),
	('warcon','i'),
	('lockedmapname','10s'),
	('lockedmaptime','i'),
	('crujob','B'),
	('cruconstructpoint','i'),
	('cruid','i'),
	('leftdeadpenaltytime','i'),
	('partyid','i'),
	('gizonitemupgradeleft', 'h'))
)