master_bank_id INT AUTO_INCREMENT PRIMARY KEY,
ifsc_first4 VARCHAR(4),
is_enach_net_active BOOLEAN DEFAULT FALSE,
is_enach_card_active BOOLEAN DEFAULT FALSE,
is_enach_esign_active BOOLEAN DEFAULT FALSE,
is_active BOOLEAN DEFAULT FALSE);