<?php
$repo = git_repository_open("/usr/opspedia/xampp");
var_dump($repo);
$reflog = git_reflog_read($repo, "HEAD");

$count = git_reflog_entrycount($reflog);
echo $count;
for($i = 0; $i < $count; $i++) {
    $entry = git_reflog_entry_byindex($reflog, $i);
    $committer = git_reflog_entry_committer($entry);
    echo "name = " . $committer['name'] . '<br/>';
}

$walker = git_revwalk_new($repo);
git_revwalk_push_range($walker, "HEAD~200..HEAD");

while($id = git_revwalk_next($walker)) {
    echo $id . "<br/>"; 
}
