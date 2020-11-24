<?php
use yii\helpers\Html;
?>

<p>You have entered the following information:</p>

<ul>
    <li><label>Name</label>: <?= html::encode($model->name) ?></li>
    <li><label>Email</label>: <?= html::encode($model->email) ?></li>
</ul>