from database_connector import DBConnector
from cryptic import Cryptic


# This will populate the table with the necessary encryption for passwords
class DBPassPopulator(DBConnector):
    def __init__(self):
        super().__init__()

    def populate(self):
        crypto = Cryptic()
        # loop through passenger passwords and encrypt them to add to the db
        passenger_passwords = ['Rb1jaXeu4', 'Kz5CS6gBdy', 'UfL7VEll3', 'Vol5C5c4', 'nm7GMMN', 'E5ZKWgugWz', 'yovvJYp9M51R', '9HJYvnaU7z', 'A3wyaHLowUy', 'XzXiMBjH', 'Mqtg874dg', 'PIi4pXKG1', 'FyBYF9PMOBQ', 'IaHrpHM', 'VcXw0j', 'UPpTFq3T', 'Qb9VF2', '9Q5ANpstk', 'UnYIhmHDJm', 'SkcuZpXbGx', '0Fa3bWRjII', 'dWt6KVWqk2Db', 'k86V29A3sQb', '8YDYNz8b', 'Er5FaWRh', 'hI1BK0h', 'tBdBIphb', 'wVQQQBtv86w', 'RDfxssYI', 'N4bJzmY6', 'eIJcW1go8TBY', 'KmJ7z8', 'iMyQpCiiK', 'uYu9wyaZIS', 'sK59i7ePo5Sa', 'PHv2sfTuDzj', 'kKwitjI', 'kt5xSvSwoC3', 'u1VbFx6zSo4', 'NTTm3owqJAwu', 'BFSa2mcV', 'Nd9ObFytbqgo', '9p5kjZJErY', 'MVu2E960v', 'BxFMAfWs3', '12LYI1Io9', 'cDMlSy5', 'FEbGXDOO3D', 'ZoymSzia0e51', 'lATdjQ4', 'IjaS641O', 'XfSkiw', 'xGcRPxaRCl', 'z2vPRNkbe', 'NLhn1NSXEvMG', 's2RGZv', 'brAb956A', 'vCJ5oCoFVi', 'PaD93lN59xb', '4l1n9A', '146ePb', 'kJdN3lVi', '1cwAcR1', 'rq2f4J1Ss7', 'IHKctP8xK', 'WXJ3MZurX', 'uiuslf9z3yR', 'gshWhlqqsnNb', 'AYp9rPjpDv', 'yJI7FbtfW9H', 'BbOCzqmU66', 'WwQMJnH038', 'tAemGLdLOpo4', 'XvolCv', 'RluN3W', 'uCTTpUP', 'hn75EwfU', '8KVzc4jXV', 'JLuDCiplgTQX', 'wbsjqW828du', 'r0tK06o4r', 'jk234A324', '2BgRQJ', 'kyWq7m', 'zs7w2wfw', 'jKuYs4ZrOEj', 'VYC0GKSWbY4', 'V8PCxlfI14Jq', '0J1W6y', 'VIW6Um', 'a01rRAdBgJ', '8KGzR4OnO7v6', 'deGGa8jcANa', 'sd4vwI', 'Or2m6C', 'u24HZT8xbgtp', 'b2zLfrXb', 'ALHvlKwxNPsp', 'zCPuFGkh', '3wYueKDuJ']
        ppas = []
        for password in passenger_passwords:
            ppas.append(crypto.encrypt(password))

        # repeat for staff passwords
        staff_passwords = ['AjfGwQW', 'bahQ2wiaU31a', 'fJjYEdD', 'nyTKb9', 'PgMXq4P1fbI', 'hFsVCDIcUpo', '7NKitRk', 'hrrne2vZsu', 'lB7zlT0UXLD', 'NgsBRmBPR', '4fALiTapQL', 'nxi1zB8', 'NXjcjS', 'Ox6F2OD8H', 'D5kAblkFu', 'JUNE7f', 'd2sPNi7r', 'au59B7', 'r3k77bgVnZbN', 'kkigNmKZA56', 'C1SvkTppdv1', 'tMYv5mzG', 'aaejTbRzTc', 'hGx0MKpE', 'QNF88D91PP', 'fNt26nrYzCun', 'PAAIE13F', 'sJRHyV', 'gbIMPY5', 'irofnuriHw', 'KiMJUtFO', 'XAyS3K', 'ZZGkvKTvQHI7', 'sltQCcOE', 'zuSriOljI', 'oKDZG0', 'DfRQAOj', 'DgdCA1VLZ', 'UZbga6n1XZ4', 'lH8mirNSpK', '9GSrP1MmxvK', 'SoI25iv', 'SsWCci9dB', 'CqxhOo4vW', 'VaTvCyf5', 'Sdl3nttVA7J', '6CWEOD6rPM', 'cBf9qB', 'ZM41s0UC1', 'MvxnB0Ho', 'Z98jUpt', 'uXJaPEn2V', 'nwO7rKmI13w', 'KUMb85P', 'NZcssFEz', '06sXlaO6', 'gKfY2d', 'KDK0xV4zX', 'qyt78p', 'tjWTon9zqM', '7IdEXkQm0', 'EarqIh', 'UlaPwWp', 'H1B9jX', 'n3rPqOyoJuP', 'ZuOy7jk7HNa', 'h8LlHMngW3F', 'o8fiD6Wwhy', 'pF6pnjVRHL', 'FQTR2wB8SOx', 'vrGd4Elmv8', 'JCuibHJjkfgI', 'QqMqWhweQPaJ', 'jQHypQA', 'VO0Zxtjz', 'vHlyxT', 'NlxKgdquGu', 'II1h6klATC4', 'pjjkqTp', 'Q8RaFT', 'zun1k6iK', 'Phremwe3u', 't9N5Ht', 'cRjkBr1bkY', 'cq10PAI', '3sXOwunEA', 'shTIBe1', '90S57vil5emY', 'GbKhXknh', 'sBsbkDjx8u', 'MhPmHHy', 'ImcxPNWME7', 'YN0JUdzo', 'GO3dGs6q0f', 'dV1zOt4u3', '0WmrC4Kit7ti', '3nsG33fOX', 'nvd73LYDsXJ', 'PudRGdf1', 'D1JHSVCSXWaJ']
        spas = []
        for password in staff_passwords:
            spas.append(crypto.encrypt(password))

        self.cursor.execute(f"""
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'vfeehily0', '{spas[0]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'sdudny1', '{spas[1]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'slauritzen2', '{spas[2]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'aidenden3', '{spas[3]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'lainslee4', '{spas[4]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'nmower5', '{spas[5]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'lteaser6', '{spas[6]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'gdunstone7', '{spas[7]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'edarlington8', '{spas[8]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'sfulep9', '{spas[9]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'apybwortha', '{spas[10]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'rhaggerstonb', '{spas[11]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'mdocwrac', '{spas[12]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'nbahlsd', '{spas[13]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'hpollette', '{spas[14]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'ljinkinf', '{spas[15]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'rayscoughg', '{spas[16]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'mgligorijevich', '{spas[17]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'nhorrodi', '{spas[18]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'jsaunperj', '{spas[19]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'jmcnerlink', '{spas[20]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'gosbidstonl', '{spas[21]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'ghryncewiczm', '{spas[22]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'amackibbonn', '{spas[23]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'btipplero', '{spas[24]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'browaszkiewiczp', '{spas[25]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'plevesqueq', '{spas[26]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'hdudingr', '{spas[27]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'gkrysiaks', '{spas[28]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (2, 'wheinot', '{spas[29]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'jcoalu', '{spas[30]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'graisbeckv', '{spas[31]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'iszachniewiczw', '{spas[32]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'mramax', '{spas[33]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cantaty', '{spas[34]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cvillaretz', '{spas[35]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'jplatts10', '{spas[36]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'adalloway11', '{spas[37]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'gyegorchenkov12', '{spas[38]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lwarren13', '{spas[39]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lyallop14', '{spas[40]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'ggelardi15', '{spas[41]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cswyne16', '{spas[42]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'tmaryska17', '{spas[43]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'tpurkis18', '{spas[44]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'uscholtz19', '{spas[45]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cvonderdell1a', '{spas[46]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'mfullerton1b', '{spas[47]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cleynton1c', '{spas[48]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'dpetty1d', '{spas[49]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'emilne1e', '{spas[50]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'amaris1f', '{spas[51]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'mpreator1g', '{spas[52]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'dadkins1h', '{spas[53]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'rguihen1i', '{spas[54]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cpalfrey1j', '{spas[55]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'dmcteer1k', '{spas[56]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'jwakes1l', '{spas[57]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'hsarjeant1m', '{spas[58]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'gsworne1n', '{spas[59]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'tgallaway1o', '{spas[60]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'mquibell1p', '{spas[61]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'abrinklow1q', '{spas[62]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'speterken1r', '{spas[63]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'ccarlsson1s', '{spas[64]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lbigg1t', '{spas[65]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'dminchenton1u', '{spas[66]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'gthaxton1v', '{spas[67]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lstirling1w', '{spas[68]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'vdyson1x', '{spas[69]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'wstaining1y', '{spas[70]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'smacgown1z', '{spas[71]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'fstitle20', '{spas[72]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'abenazet21', '{spas[73]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'fcrawshaw22', '{spas[74]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'amaccauley23', '{spas[75]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lhowden24', '{spas[76]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'carnaudot25', '{spas[77]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'jepsly26', '{spas[78]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'dpoint27', '{spas[79]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lmagrannell28', '{spas[80]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lschirak29', '{spas[81]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lfenkel2a', '{spas[82]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'mmcgraffin2b', '{spas[83]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'mdarter2c', '{spas[84]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'ccheng2d', '{spas[85]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'dbrinkler2e', '{spas[86]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'rkobieriecki2f', '{spas[87]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'bjirek2g', '{spas[88]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'enewiss2h', '{spas[89]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cparkyn2i', '{spas[90]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'njeffs2j', '{spas[91]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'ecurnok2k', '{spas[92]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'kivatt2l', '{spas[93]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'spieche2m', '{spas[94]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'vcanter2n', '{spas[95]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'abattlestone2o', '{spas[96]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'erown2p', '{spas[97]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'cdillicate2q', '{spas[98]}');
        INSERT INTO StaffLogins (StaffLevel, StaffUsername, StaffPassword) VALUES (1, 'lcawse2r', '{spas[99]}');

        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('skingswell0', '{ppas[0]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('umcian1', '{ppas[1]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('wpohlke2', '{ppas[2]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rbilton3', '{ppas[3]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('tweald4', '{ppas[4]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('lretchless5', '{ppas[5]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('tlaycock6', '{ppas[6]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('atattoo7', '{ppas[7]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ulesieur8', '{ppas[8]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('bseear9', '{ppas[9]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('gtankarda', '{ppas[10]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('cfillinghamb', '{ppas[11]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('oalphegec', '{ppas[12]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rquigd', '{ppas[13]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('klampe', '{ppas[14]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('lmccaskillf', '{ppas[15]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('kjulianog', '{ppas[16]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('igreweh', '{ppas[17]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('otothi', '{ppas[18]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('mworsellj', '{ppas[19]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('cpollardk', '{ppas[20]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('czaninil', '{ppas[21]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('kmellenbym', '{ppas[22]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('zdaintiern', '{ppas[23]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('cbuckleeo', '{ppas[24]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('mmanclarkp', '{ppas[25]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('gburyq', '{ppas[26]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('vcavenr', '{ppas[27]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('nsergeants', '{ppas[28]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('tcullernet', '{ppas[29]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('fburdittu', '{ppas[30]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('sselesnickv', '{ppas[31]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ycolemanw', '{ppas[32]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('nboicex', '{ppas[33]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ebenezy', '{ppas[34]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('lmcsperronz', '{ppas[35]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('iyankeev10', '{ppas[36]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('cpeplow11', '{ppas[37]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('swisden12', '{ppas[38]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('bdominichelli13', '{ppas[39]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('eyeowell14', '{ppas[40]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('koscannill15', '{ppas[41]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('agibbings16', '{ppas[42]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ldiggell17', '{ppas[43]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('mholbie18', '{ppas[44]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('pbranscombe19', '{ppas[45]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('cconnikie1a', '{ppas[46]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('oantcliffe1b', '{ppas[47]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('edederick1c', '{ppas[48]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('aconeau1d', '{ppas[49]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('dkennefick1e', '{ppas[50]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('selstow1f', '{ppas[51]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('iklimecki1g', '{ppas[52]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rwindebank1h', '{ppas[53]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('bkimbley1i', '{ppas[54]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('dnaper1j', '{ppas[55]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('spolle1k', '{ppas[56]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('droskelly1l', '{ppas[57]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('kaspell1m', '{ppas[58]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('jnewiss1n', '{ppas[59]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rpharaoh1o', '{ppas[60]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('cruddock1p', '{ppas[61]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('lcollen1q', '{ppas[62]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rberthon1r', '{ppas[63]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ggrindle1s', '{ppas[64]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rtournie1t', '{ppas[65]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('gclute1u', '{ppas[66]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('bkirman1v', '{ppas[67]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('zhaysman1w', '{ppas[68]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('blemme1x', '{ppas[69]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('akielty1y', '{ppas[70]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('dendrizzi1z', '{ppas[71]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('fmessitt20', '{ppas[72]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('vbielfelt21', '{ppas[73]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ztucknott22', '{ppas[74]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('dbaudi23', '{ppas[75]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('sgainsburgh24', '{ppas[76]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rschops25', '{ppas[77]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('pmckeveney26', '{ppas[78]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('jsumnall27', '{ppas[79]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('pskupinski28', '{ppas[80]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('SwAP3SyY', '{ppas[81]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('swrack2a', '{ppas[82]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('mbranche2b', '{ppas[83]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('jwardlaw2c', '{ppas[84]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('lpottle2d', '{ppas[85]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('deastcourt2e', '{ppas[86]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ldanjoie2f', '{ppas[87]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('vriding2g', '{ppas[88]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('tleguin2h', '{ppas[89]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('clockey2i', '{ppas[90]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('cstandall2j', '{ppas[91]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('jpardew2k', '{ppas[92]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('akennler2l', '{ppas[93]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('rhaughton2m', '{ppas[94]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('akeely2n', '{ppas[95]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('bjeffcoat2o', '{ppas[96]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('zbarkhouse2p', '{ppas[97]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('ycollcutt2q', '{ppas[98]}');
        INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('troadknight2r', '{ppas[99]}');""")
        self.db_connection.commit()

if __name__ == "__main__":
    populate = DBPassPopulator()
    populate.populate()