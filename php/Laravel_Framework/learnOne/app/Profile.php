<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Profile extends Model
{
    protected $guarded = [];
    
    public function profileImage()
    {
        $imagePath = ($this->image) ? $this->image : 'profile/EFGctYFo4oqprfNi0CmYPrt1xyeO0jYp7Le7SAxv.jpeg';
        return '/storage/' . $imagePath;
    }

    public function User()
    {
        return $this->belongsTo(User::class);
    }
}
